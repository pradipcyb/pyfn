"""Unmarshall SemEval 2007 FrameNet XML files."""

import logging
import xml.etree.ElementTree as element_tree

import pyfn.marshalling.unmarshallers.framenet as fn_unmarshaller

__all__ = ['unmarshall_semeval07_xml']

logger = logging.getLogger(__name__)


def unmarshall_semeval07_xml(xml_file_path, flatten=False):
    """Unmarshall a SemEval 2007 FrameNet XML file from file path.

    Return a generator of AnnotationSet instances extracted from the
    XML file. A single list of AnnotationSet instances corresponds
    to all the AnnotationSets of a single Sentence.

    Args
    ----
        param1 xml_files_path: full path to a SemEval 2007 FrameNet XML file.

    """
    logger.info('Unmarshalling SemEval FrameNet XML file: {}'
                .format(xml_file_path))
    # pylint: disable=R1702
    for documents_tag in element_tree.parse(xml_file_path).getroot().findall(
            'documents'):
        for document_tag in documents_tag.findall('document'):
            for paragraphs_tag in document_tag.findall('paragraphs'):
                for paragraph_tag in paragraphs_tag.findall('paragraph'):
                    for sentences_tag in paragraph_tag.findall('sentences'):
                        for sentence_tag in sentences_tag.findall('sentence'):
                            annosets = fn_unmarshaller.extract_fn_annosets(
                                sentence_tag, xml_schema_type='semeval')
                            if annosets:
                                if not flatten:
                                    yield annosets
                                if flatten:
                                    for annoset in annosets:
                                        yield annoset