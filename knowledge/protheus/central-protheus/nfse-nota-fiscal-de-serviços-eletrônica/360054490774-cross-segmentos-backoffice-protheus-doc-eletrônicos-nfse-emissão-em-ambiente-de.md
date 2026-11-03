---
article_id: 360054490774
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3f78742513454c63b0e05dae10c491662129f0633335d9e48b24c2f5ff4f7e55
fetched_at: '2026-06-28T22:39:57.415728+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - EMISSÃO EM
  AMBIENTE DE HOMOLOGAÇÃO (São Paulo)
type: support-article
updated_at: '2025-06-20T11:55:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054490774-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-EMISS%C3%83O-EM-AMBIENTE-DE-HOMOLOGA%C3%87%C3%83O-S%C3%A3o-Paulo
---

**Dúvida**Como realizar a transmissão de um RPS para a prefeitura de SP no ambiente de homologação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para enviar uma nota no ambiente de homologação para a prefeitura de SP basta configurar o Wizard.cfg e alterar o campo Ambiente:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094340433/mceclip0.png)  
  
Vale lembrar que a prefeitura não converte em NFSe o RPS transmitido, portanto não retorna o número da NFSe.  
Por padrão o TSS mantem da seguinte forma na autorização de **TODAS as notas transmitidas em homologação** para essa prefeitura.  
  
NFSE: 0  
PROTOCOLO: NFSE\_HOM   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092129194/mceclip1.png)  
  
**IMPORTANTE**Apesar de não converter o RPS em NFSe no ambiente de homologação, por se tratar de utilizar a mesma URL, a prefeitura realiza as mesmas validações pois tratam em um único banco de dados ambos os ambientes.  
  
Portanto, conforme item 4.3.4 no [manual da prefeitura](http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais-arquivos/nfe_web_service.pdf/@@download/file/NFe_Web_Service.pdf), **é indicado a utilização desse ambiente apenas na implantação**, caso já tenha sido transmitido em Produção via Web Service, evite a utilização desse ambiente, pois seu uso resultará em duplicidade de esforços desnecessários, pois as verificações feitas no método TesteEnvioLoteRPS (homologação) são as mesmas realizadas pelo método EnvioLoteRPS (produção).  
  
Exemplo: Transmitir com a mesma numeração/série em homologação, de uma nota já autorizada em produção, a prefeitura retornará: '224 - RPS já convertida em NFSe'.  
 *Observações.:  
- O cancelamento em homologação não é possível ser realizado. Detalhes: [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052697193-MP-NFSE-S%C3%83O-PAULO-SP-CANCELAMENTO-EM-AMBIENTE-DE-HOMOLOGA%C3%87%C3%83O)*  
*- Se faz necessário o uso do certificado digital, assim como em produção.*
