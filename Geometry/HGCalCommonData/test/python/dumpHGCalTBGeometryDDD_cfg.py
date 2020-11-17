import FWCore.ParameterSet.Config as cms

process = cms.Process("DUMP")
process.load("Geometry.HGCalCommonData.testTB181V0XML_cfi")
process.load('FWCore.MessageService.MessageLogger_cfi')


    
    
    

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.add_(cms.ESProducer("TGeoMgrFromDdd",
    verbose = cms.untracked.bool(False),
    level   = cms.untracked.int32(14)
))

process.dump = cms.EDAnalyzer("DumpSimGeometry",
                              outputFileName = cms.untracked.string('tbModuleXDDD.root'))

process.p = cms.Path(process.dump)
