---
content_hash: f5d0f1a6c3f6a9c4ab65cbdca10514e40c276c9b55313b6b2c79e77c82ddb460
fetched_at: '2026-06-29T00:08:33.383221+00:00'
page_id: '274315268'
product: rm
source: tdn-rm
title: RPTMIG00009.4.1 - Page Settings
type: documentation
url: https://tdn.totvs.com/display/LRM/RPTMIG00009.4.1+-+Page+Settings
version: 6
---

# Page Settings

|  |  |
| --- | --- |
| **Produto:** | Totvs Reports |
| **Versões:** | 12.1.x |
| **Ocorrência:** |  |
| **Ambiente:** |  |
| **Passo a passo:** | Conteúdo  ---  Conteúdo|Nomear / Renomear Controles|Galeria Consulta SQL Vinculada a Banda|Galeria Consulta SQL Não Vinculada a BandaIntrodução  ---     Com o advento da migração do **TOTVS Reports** da **versão 11.8x** para as versões **superiores a versão 12.1.4**, muitas alterações foram feitas principalmente **na geração sobre demanda dos dados** vinculados a cada componente presente no relatório.  Em relatórios da versão **11.8x**, por exemplo, **a geração sobre demanda dos dados** era realizada no momento da impressão de cada componente, ao contrário dos das versões mais atuais **(12.1.5 ou superiores)**, onde a geração dos dados é feita através de apenas uma consulta SQL **(Fase de Preparação)**, que é gerada a partir das tabelas e consultas SQL vinculadas ao relatório. 1 - Page Settings  ---     Com a migração para a nova versão do Reports, a compatibilidade de algumas funcionalidades não puderam ser mantidas:  Isso se deve ao fato de como o Relatório é montado e disponibilizado para apresentação.    Na versão **11.8x**, todos os dados do relatório eram gerados sob-demanda, ou seja, no momento da geração, as **consultas SQL**, e/ou **expressões** e/ou **fórmulas** e/ou **totalizadores** eram executados. O ponto negativo disso é que **consultas SQL** **(vinculadas ao campos texto, expressões)** eram executadas várias vezes, onerando o tempo de geração do relatório.  Na versão **12.1.x**, **os dados são recuperados primeiro** e **depois** na geração do relatório **os componentes são executados**. O que contribui para melhor performance dos relatórios.    Na versão **11.8x**, o documento é criado, o layout é carregado e os dados posteriormente obtidos e apresentados. **(Os relatórios eram gerados, em sua maioria, pelo lado "client', o que conferia a funcionalidade de editar as propriedades da página)**.  Na versão **12.1.x**, os dados são obtidos através de um **SQL geral**, o documento é criado e salvo, o layout é carregado e após isso, os dados são apresentados. **(Os relatórios são gerados exclusivamente pelo server, através de uma API, para comunicação com o lado client, o que deixa de conferir a funcionalidade de editar as propriedades da página).**   1.1 - Page Settings - Funcionalidades Desabilitadas  ---     As funcionalidades desabilitadas na versão **12.1.x** são:       1. **Customization (Personalização)** 2. **Page Setup (Propriedades da Página / Configuração da Página)** 3. **Header and Footer (Cabeçalho e Rodapé)** 4. **Scale (Escala)**   **OBS: A edição de margens também foi desabilitada.** |
| **Observações:** |  |
