model_string = f"""
    function MM(km, Vmax, S)
        Vmax * S / (km + S)
    end

    function MMWithKcat(km, kcat, S, E)
        kcat * E * S / (km + S)
    end

    function NonCompetitiveInhibition(km, ki, Vmax, n, I, S)
        Vmax * S / ( (km + S) * (1 + (I / ki)^n ) )
    end

    function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
        kcat * E * S / ( (km + S) * (1 + (I / ki)^n ) )
    end

    function NonCompetitiveInhibitionWithKcatAndExtraActivator(km, ki, kcat, E1, E2, n, I, S)
        kcat * E1 * E2 * S / ( (km + S) * (1 + (I / ki)^n ) )
    end


    function MA1(k, S)
        k * S
    end

    function MA2(k, S1, S2)
        k * S1 * S2
    end

    function MA1Mod(k, S, M)
        k * S * M
    end

    function MA2Mod(k, S1, S2, M)
        k * S1 * S2 * M
    end

    function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
        kcat * E * S / (km + S + ((km * I )/ ki)  )
    end

    function CompetitiveInhibition(Vmax, km, ki, I, S)
        Vmax * S / (km + S + ((km * I )/ ki)  )
    end

    function Hill(km, kcat, L, S, h)
        kcat * L * (S / km)^h  /   1 + (S / km)^h
    end

    model AktModelWithMMRateLaws()
        compartment             Cell = 1;
        var IRS1                in Cell;
        var IRS1a               in Cell;
        var IRS1pS636_639       in Cell;
        var Akt                 in Cell;
        var AktpT308            in Cell;
        var TSC2                in Cell;
        var TSC2pT1462          in Cell;
        var PRAS40              in Cell;
        var PRAS40pT246         in Cell;
        var S6K                 in Cell;
        var S6KpT389            in Cell;
        var FourEBP1            in Cell;
        var FourEBP1pT37_46     in Cell;
        var _PI3K               in Cell;
        var pPI3K               in Cell;
        var pmTORC1             in Cell;
        var _mTORC1             in Cell;
        const Insulin           in Cell;
        const AA                in Cell;

        // global variables
        Insulin = 1;
        AA = 1

        IRS1            = 10;
        IRS1a           = 0.1;
        IRS1pS636_639   = 0.1;
        _PI3K            = 10;
        pPI3K           = 0.1;
        AktpT308        = 0.1;
        Akt             = 10;
        TSC2pT1462      = 10;
        TSC2            = 0.1;
        pmTORC1         = 0.1;
        _mTORC1cyt       = 10;
        mTORC1lys       = 0.1;
        PRAS40          = 10;
        PRAS40pT246     = 0.1;
        FourEBP1pT37_46 = 0.1;
        FourEBP1        = 10;
        S6KpT389        = 0.1;
        S6K             = 10;

        // kinetic parameters
        _kIRS1In                  = 1;                      
        _kIRS1Out                 = 1;                     
        _kIRS1Out2                = 1;                    
        _kIRS1ActBasal            = 1;                        
        _kIRS1Act_km              = 1;                          
        _kIRS1Act_kcat            = 1;                        
        kIRS1Inact                = 1;                    
        _kIRS1Phos_km             = 1;                         
        _kIRS1Phos_kcat           = 1;                       
        _kPI3KPhos_km             = 1;                         
        _kPI3KPhos_kcat           = 1;                       
        kPI3KDephos               = 1;                   
        _kAktPhos_km              = 1;                          
        _kAktPhos_kcat            = 1;                        
        kAktDephos                = 1;                    
        _kAktIn                   = 1;               
        _kAktOut                  = 1;                      
        _kTSC2Phos_km             = 1;                         
        _kTSC2Phos_kcat           = 1;                       
        _kTSC2Dephos              = 1;                          
        _kTSCIn                   = 1;               
        _kTSCOut                  = 1;                      
        _kmTORC1PhosBasal         = 1;                             
        _kmTORC1Phos_km           = 1;                       
        _kmTORC1Phos_vmax         = 1;                             
        _kmTORC1Dephos_km         = 1;                             
        _kmTORC1Dephos_kcat       = 1;                           
        _kPras40In                = 1;                    
        _kPras40Out               = 1;                   
        _kPras40Phos_km           = 1;                       
        _kPras40Phos_kcat         = 1;                             
        kPras40Dephos             = 1;                         
        _kFourEBP1In              = 1;                          
        _kFourEBP1Out             = 1;                         
        _kFourEBP1Phos_km         = 1;                             
        _kFourEBP1Phos_kcat       = 1;                           
        kFourEBP1Dephos           = 1;                       
        _kS6KIn                   = 1;               
        _kS6KOut                  = 1;                      
        _kS6KPhos_km              = 1;                          
        _kS6KPhos_kcat            = 1;                        
        kS6KDephos                = 1;                    
        
        _IRS1pS636_639_sf        = 1;        
        _AktpT308_sf             = 1;
        _TSC2pT1462_sf           = 1;    
        _PRAS40pT246_sf          = 1;    
        _FourEBP1pT37_46_sf      = 1;        
        _S6KpT389_sf             = 1;

        IRS1pS636_639_obs           := IRS1pS636_639 / _IRS1pS636_639_sf ;       
        AktpT308_obs                := AktpT308 / _AktpT308_sf ;   
        TSC2pT1462_obs              := TSC2pT1462 / _TSC2pT1462_sf ;   
        PRAS40pT246_obs             := PRAS40pT246 / _PRAS40pT246_sf ;   
        FourEBP1pT37_46_obs         := FourEBP1pT37_46 / _FourEBP1pT37_46_sf ;       
        S6KpT389_obs                := S6KpT389 / _S6KpT389_sf ;   

        // reactions // MMWithKcat(km, kcat, S, E)
        // function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
        // function MM(km, Vmax, S)
        // function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
        R1In    : => IRS1                               ; Cell * _kIRS1In;
        R1Out   : IRS1 =>                               ; Cell * _kIRS1Out*IRS1;
        R1Out2  : IRS1pS636_639  =>                     ; Cell * _kIRS1Out2*IRS1pS636_639;
        R1Basal : IRS1 => IRS1a                         ; Cell * _kIRS1ActBasal*IRS1;
        R1f1    : IRS1 => IRS1a                         ; Cell * MMWithKcat(_kIRS1Act_km, _kIRS1Act_kcat, IRS1, Insulin);
        R1b     : IRS1a => IRS1                         ; Cell * kIRS1Inact*IRS1a;
        R1f2    : IRS1a => IRS1pS636_639                ; Cell * MMWithKcat(_kIRS1Phos_km, _kIRS1Phos_kcat, IRS1a, S6KpT389);
        R3f     : _PI3K => pPI3K                         ; Cell * MMWithKcat(_kPI3KPhos_km, _kPI3KPhos_kcat, _PI3K, IRS1a);
        R3b     : pPI3K => _PI3K                         ; Cell * kPI3KDephos*pPI3K;
        R4f     : Akt => AktpT308                       ; Cell * MMWithKcat(_kAktPhos_km, _kAktPhos_kcat, Akt, pPI3K);
        R4b     : AktpT308 => Akt                       ; Cell * kAktDephos*pPI3K*AktpT308;
        R4In    : => Akt                                ; Cell * _kAktIn;
        R4Out   : Akt =>                                ; Cell * _kAktOut*Akt;
        R5f     : TSC2 => TSC2pT1462                    ; Cell * MMWithKcat(_kTSC2Phos_km, _kTSC2Phos_kcat, TSC2, AktpT308);
        R5b     : TSC2pT1462 => TSC2                    ; Cell * _kTSC2Dephos*TSC2pT1462;
        R5In    : => TSC2                               ; Cell * _kTSCIn;
        R5Out   : TSC2 =>                               ; Cell * _kTSCOut*TSC2;
        R6Basal : _mTORC1 => pmTORC1                    ; Cell * _kmTORC1PhosBasal*_mTORC1; 
        R6f     : _mTORC1 => pmTORC1                    ; Cell * MM(_kmTORC1Phos_km, _kmTORC1Phos_vmax, mTORC1); 
        R6b     : pmTORC1 => _mTORC1                    ; Cell * MMWithKcat(_kmTORC1Dephos_km, _kmTORC1Dephos_kcat, pmTORC1, TSC);
        R8In    : => PRAS40                             ; Cell * _kPras40In;
        R8Out   : PRAS40 =>                             ; Cell * _kPras40Out*PRAS40;
        R8f     : PRAS40 => PRAS40pT246                 ; Cell * MMWithKcat(_kPras40Phos_km, _kPras40Phos_kcat, PRAS40, AktpT308);
        R8b     : PRAS40pT246 => PRAS40                 ; Cell * kPras40Dephos*PRAS40pT246;
        R9In    : => FourEBP1                           ; Cell * _kFourEBP1In;
        R9Out   : FourEBP1 =>                           ; Cell * _kFourEBP1Out*FourEBP1;
        R9f     : FourEBP1 => FourEBP1pT37_46           ; Cell * MMWithKcat(_kFourEBP1Phos_km, _kFourEBP1Phos_kcat, FourEBP1, pmTORC1);
        R9b     : FourEBP1pT37_46 => FourEBP1           ; Cell * kFourEBP1Dephos*FourEBP1pT37_46;
        R10In   : => S6K                                ; Cell * _kS6KIn;
        R10Out  : S6K =>                                ; Cell * _kS6KOut*S6K;
        R10f    : S6K => S6KpT389                       ; Cell * MMWithKcat(_kS6KPhos_km, _kS6KPhos_kcat, S6K, pmTORC1);
        R10b    : S6KpT389 => S6K                       ; Cell * kS6KDephos*S6KpT389;

    end

    """