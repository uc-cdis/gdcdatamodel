from edge import Edge


class MemberOf(object):
    __label__ = 'member_of'


class ParticipantMemberOfProject(Edge, MemberOf):
    __src_label__ = 'participant'
    __dst_label__ = 'project'


class ProjectMemberOfProgram(Edge, MemberOf):
    __src_label__ = 'project'
    __dst_label__ = 'program'


class ArchiveMemberOfProject(Edge, MemberOf):
    __src_label__ = 'archive'
    __dst_label__ = 'project'


class FileMemberOfArchive(Edge, MemberOf):
    __src_label__ = 'file'
    __dst_label__ = 'archive'


class FileMemberOfExperimentalStrategy(Edge, MemberOf):
    __src_label__ = 'file'
    __dst_label__ = 'experimental_strategy'


class FileMemberOfDataSubtype(Edge, MemberOf):
    __src_label__ = 'file'
    __dst_label__ = 'data_subtype'


class FileMemberOfDataFormat(Edge, MemberOf):
    __src_label__ = 'file'
    __dst_label__ = 'data_format'


class FileMemeberOfTag(Edge, MemberOf):
    __src_label__ = 'file'
    __dst_label__ = 'tag'


class DataSubtypeMemberOfDataType(Edge, MemberOf):
    __src_label__ = 'data_subtype'
    __dst_label__ = 'data_type'
