import FWCore.ParameterSet.Config as cms

topDecayChannelChecker = cms.EDAnalyzer('TopDecayChannelChecker',
  ## input collection; this maybe any collection of type
  ## reco::GenParticles.
  src = cms.InputTag('genParticles'),
                                        
  ## name of the root output file that will contain the
  ## histograms.
  outputFile = cms.string('TopDecayChannelChecker.root'),

  ## number of events for which a full partile listing
  ## will be printed into the logfile. 0 will switch
  ## this kind of logging off.
  logEvents = cms.uint32(10)
)
