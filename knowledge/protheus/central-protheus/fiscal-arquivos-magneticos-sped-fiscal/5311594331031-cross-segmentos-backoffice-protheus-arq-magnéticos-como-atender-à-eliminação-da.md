---
article_id: 5311594331031
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 0c95fee07a42a2acd1b00276969bba03db1515ed66c34e6377e0918370b99f93
fetched_at: '2026-06-28T22:42:00.817526+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Arq. Magnéticos - Como atender à Eliminação
  da GIA SP na geração do Sped Fiscal?
type: support-article
updated_at: '2022-07-25T16:49:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5311594331031-Cross-Segmentos-Backoffice-Protheus-Arq-Magn%C3%A9ticos-Como-atender-%C3%A0-Elimina%C3%A7%C3%A3o-da-GIA-SP-na-gera%C3%A7%C3%A3o-do-Sped-Fiscal
---

**Dúvida**Como atender à **Eliminação da GIA SP** na geração do **Sped Fiscal?**  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

A **Eliminação da GIA** refere-se à dispensa da obrigação, pelo contribuinte paulista, de entregar mensalmente a **GIA**, tendo em vista que a **SEFAZ-SP** gerará automaticamente uma **GIA** virtual a partir da **EFD ICMS/IPI.**

Para isso, foi necessário abrir a possibilidade para que sejam declarados, na **EFD,** os valores das colunas:

**- Outras;**  
**- Isentas/Não Tributadas;**  
**- ICMS-ST na condição de substituído.**Para atender a eliminação da **GIA SP** e  atender à **CAT66** avalie as informações contidas nos links abaixo:

Como gerar o Registro **0460** do **Sped Fiscal**?  
[MP - FIS - SPED FISCAL - REGISTRO 0450 e 0460](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316511-MP-FIS-SPED-FISCAL-REGISTRO-0450-e-0460?source=search)

Como gerar os Registros **C190, C195 e C197**?  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010170492-REGISTRO-C190-C195-e-C197](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010170492-REGISTRO-C190-C195-e-C197&sa=D&source=hangouts&ust=1597845127969000&usg=AFQjCNHHy5QwIAzYP_CmdWeaPMuBZ_z-Zw)

Informações dos códigos de reflexo conforme **Portaria CAT66**  
<https://tdn.totvs.com/display/public/PROT/FIS0024_Portaria_CAT66_SP>  
  
Como preencher o **campo 03 do C197/D197**  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028644591-MP-FIS-SPEDFISCAL-Como-preencher-o-campo-03-DESCR-COMPL-AJ-Descri%C3%A7%C3%A3o-complementar-do-ajuste-do-documento-no-Registro-C197>  
  
Para gerar os Registros **C197 e D197** com os códigos de ajustes de lançamento será necessário amarrar um **Código de Reflexo** no cadastro de **TES** que determine quais serão os valores da nota a serem considerados para esses códigos.  
  
Abaixo segue link com informações quanto ao conceito da configuração do **Código de Reflexo (FISA072).** Em caso de dúvidas quanto à configuração do **Código de Reflexo** contate o time de Escrituração Fiscal, pois a correta configuração deste é essencial para que os dados sejam gravados na **tabela CDA.**  
  
A partir da gravação da tabela **CDA,** é que os dados serão buscados para gerar os registros **C197 e D197** no **Sped Fiscal.** Dessa forma, caso após realizar as devidas configurações, se o registro não for gerado, primeiramente valide se a tabela em questão foi gravada.   
Se não tiver sido gravada é porque há alguma inconsistência na configuração do código de reflexo, por isso, verifique o link abaixo:

[MP - FIS - Configuração Códigos de Reflexo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042440814-MP-FIS-Configura%C3%A7%C3%A3o-C%C3%B3digos-de-Reflexo?source=search)
