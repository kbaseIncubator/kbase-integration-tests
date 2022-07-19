/*
KBase genome ID
@id kb
*/
typedef string Genome_id;

/*
ContigSet contig ID
@id external
*/
typedef string Contig_id;

/*
Reference to a source_id
@id external
*/
typedef string source_id;

/*
Structure for a publication (from ER API)
also want to capture authors, journal name (not in ER)
*/
typedef tuple<int, string, string, string, string, string, string> publication;

/*
Genome feature ID
@id external
*/
typedef string Feature_id;

/*
Structure for a protein family
        @optional query_begin query_end subject_begin subject_end score evalue subject_description release_version
*/
typedef structure {
  string id;
  string subject_db;
  string release_version;
  string subject_description;
  int query_begin;
  int query_end;
  int subject_begin;
  int subject_end;
  float score;
  float evalue;
} ProteinFamily;

/*
a notation by a curator of the genome object
*/
typedef tuple<string, string, int> annotation;

/*
Structure for subsystem data (from CDMI API)
*/
typedef tuple<string, string, string> subsystem_data;

/*
Structure for regulon data (from CDMI API)
*/
typedef tuple<string, list<Feature_id>, list<Feature_id>> regulon_data;

/*
Structure for an atomic regulon (from CDMI API)
*/
typedef tuple<string, int> atomic_regulon;

/*
Structure for coexpressed fids (from CDMI API)
*/
typedef tuple<Feature_id, float> coexpressed_fid;

/*
Structure for co-occurring fids (from CDMI API)
*/
typedef tuple<Feature_id, float> co_occurring_fid;

/*
Structure for a single feature of a Feature
        Should genome_id contain the genome_id in the Genome object,
        the workspace id of the Genome object, a genomeref,
        something else?
        Should sequence be in separate objects too?
        We may want to add additional fields for other CDM functions
        (e.g., atomic regulons, coexpressed fids, co_occurring fids,...)

    @optional md5 location function protein_translation protein_families subsystems publications subsystems subsystem_data aliases annotations regulon_data atomic_regulons coexpressed_fids co_occurring_fids dna_sequence protein_translation_length dna_sequence_length
    @searchable ws_subset id type function aliases md5
*/
typedef structure {
  Feature_id id;
  list<tuple<Contig_id, int, string, int>> location;
  string type;
  string function;
  string md5;
  string protein_translation;
  string dna_sequence;
  int protein_translation_length;
  int dna_sequence_length;
  list<publication> publications;
  list<string> subsystems;
  list<ProteinFamily> protein_families;
  list<string> aliases;
  list<annotation> annotations;
  list<subsystem_data> subsystem_data;
  list<regulon_data> regulon_data;
  list<atomic_regulon> atomic_regulons;
  list<coexpressed_fid> coexpressed_fids;
  list<co_occurring_fid> co_occurring_fids;
} Feature;

/*
Reference to a ContigSet object containing the contigs for this genome in the workspace
    @id ws KBaseGenomes.ContigSet
*/
typedef string ContigSet_ref;

/*
Reference to a ProteinSet object containing the proteins for this genome in the workspace
@id ws KBaseGenomes.ProteinSet
*/
typedef string ProteinSet_ref;

/*
Reference to a TranscriptSet object containing the transcripts for this genome in the workspace
@id ws KBaseGenomes.TranscriptSet
*/
typedef string TranscriptSet_ref;

/*
Genome object holds much of the data relevant for a genome in KBase
        Genome publications should be papers about the genome, not
        papers about certain features of the genome (which go into the
        Feature object)
        Should the Genome object have a list of feature ids? (in
        addition to having a list of feature_refs)
        Should the Genome object contain a list of contig_ids too?

@optional contig_ids publications md5 taxonomy gc_content complete dna_size num_contigs contig_lengths contigset_ref proteinset_ref transcriptset_ref
@searchable ws_subset features.[*].(md5,id,type,function,aliases) taxonomy num_contigs source_id source genetic_code id scientific_name domain contigset_ref proteinset_ref transcriptset_ref
*/
typedef structure {
  Genome_id id;
  string scientific_name;
  string domain;
  int genetic_code;
  int dna_size;
  int num_contigs;
  list<int> contig_lengths;
  list<Contig_id> contig_ids;
  string source;
  source_id source_id;
  string md5;
  string taxonomy;
  float gc_content;
  int complete;
  list<publication> publications;
  list<Feature> features;
  ContigSet_ref contigset_ref;
  ProteinSet_ref proteinset_ref;
  TranscriptSet_ref transcriptset_ref;
} Genome;