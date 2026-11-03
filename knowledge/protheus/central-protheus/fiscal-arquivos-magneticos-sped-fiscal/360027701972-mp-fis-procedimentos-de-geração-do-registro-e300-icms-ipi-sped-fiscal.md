---
article_id: 360027701972
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: a9cd482578b7451b80ef4a6533b97020e7a7cf91ae6320325078b38a27036d06
fetched_at: '2026-06-28T22:42:03.803688+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'MP - FIS - Procedimentos de Geração do Registro E300 - ICMS IPI - SPED FISCAL '
type: support-article
updated_at: '2021-04-28T14:25:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027701972-MP-FIS-Procedimentos-de-Gera%C3%A7%C3%A3o-do-Registro-E300-ICMS-IPI-SPED-FISCAL
---

**Dúvida**Procedimentos de geração do registro E300: Período de Apuração do Fundo de Combate à Pobreza e do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15   
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Os registros da família **E300** serão gerados a partir das tabelas **F0I - Apuração Difal/FECP, F0J - Guias/Títulos DIFAL/FECP e F0K - Código de Lançamento Apuração DIFAL/FECP.**Esta tabelas são populadas através da apuração do ICMS MATA953, ou seja, para geração dos registros E300 será necessário que apuração do ICMS tenha sido processada.

#### **REGISTRO E311: AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS DIFERENCIAL DE ALÍQUOTA UF ORIGEM/DESTINO EC 87/15.**

Este registro irá demonstrar as informações do documento fiscal atrelado com um código de ajuste de apuração do Difal. As informações deste registro terão origem das tabelas SFT e F0K

| Campo do Registro E313 | Origem da Informação |
| --- | --- |
| 01 – REG | Texto fixo “E313” |
| 02 – COD\_PART | Código do FT\_CLIEFOR gerado no registro 0150 |
| 03 – COD\_MOD | Modelo do Documento (FT\_ESPECIE) |
| 04 – SER | FT\_SERIE |
| 05 – SUB | "" |
| 06 – NUM\_DOC | FT\_NFISCAL |
| 07 – CHV\_DOCe | FT\_CHVNFE |
| 08 – DT\_DOC | FT\_EMISSAO |
| 09 – COD\_ITEM | Código do FT\_PRODUTO gerado no registro 0200 |
| 10 – VL\_AJ\_ITEM | CDA\_VALOR |

Realizar Ajusta na Apuração de ICMS Aba DIFAL/FECP – Rotina MATA953  
  
**Caminho Protheus -> Modulo Livros fiscais/Miscelânea/Apurações/Apuração de ICMS**  
  
**![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2020%3A55%3A1.png?version=1&modificationDate=1466290135000&api=v2)**  
  
Deverá ser selecionado a linha do estado onde será realizado ajuste e efetuar duplo click será apresentado tela abaixo.  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2020%3A55%3A29.png?version=1&modificationDate=1466290163000&api=v2)  
  
Deverá ser selecionado linha da aba DIFAL/FECAP onde será realizado lançamento de ajuste na apuração.  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2020%3A55%3A49.png?version=1&modificationDate=1466290182000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2020%3A57%3A24.png?version=1&modificationDate=1466290278000&api=v2)  
  
Após incluir linha será apresentado uma nova linha abaixo da linha 002 conforme imagem abaixo  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2020%3A58%3A2.png?version=1&modificationDate=1466290316000&api=v2)  
  
Importante  
**2.4.1** - Na nova linha na coluna Código marcada com a cor verde deve ser informado o código do subitem exemplo 002.01  
  
**2.4.2** – A coluna Lanc.  onde existe a letra 2-MANUAL é para informa que o lançamento é manual incluído direto na apuração.  
  
**2.4.3**- Na nova linha na coluna Cod. Lançamento com cor Verde deve ser informado o Código de ajuste da apuração tabela 5.1.1 da receita gravadas na tabela CDO referente a cada estado.  
  
Para importar os códigos da receita na tabela CDO referente ao DIFAL deve ser realizado processo abaixo.  
CDO – 5.1.1 Publicada no site do SPED como Ajustes dos Saldos da Apuração do ICMS  
  
Para alimentar ou atualizar a tabela CDO - Ajustes manuais de apuração de ICMS é necessário seguir os seguintes passos.  
  
\*\* Acesse site da receita:  
<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>  
  
\*\* Selecionar Tabelas de Seu Estado  
(Caso Estado selecionado não possua códigos de Ajuste de ICMS (Exemplo estado de São Paulo), poderá ser utilizado Tabela Genérica de ICMS "Selecionar Tabelas Genéricas - ICMS")  
  
 \*\* Baixar Ajustes dos Saldos da Apuração do ICMS (Arquivo TXT)  
  
 \*\* Coloque o Arquivo TXT dentro da pasta Protheus\_data/ System  
  
 \*\* Inicialize Protheus utilizado "programa inicial" como U\_IMPSPED  
  
 Durante o processo será feita pergunta (deseja efetuar a importação das informações cadastrais do SPED?) Selecione botão SIM  
  
\*\* Selecione a pasta que está o arquivo TXT (Protheus\_data / System)  
  
Após continuar processo será exibido relatório com as tabelas atualizadas.  
  
A tabela CDO está atualizada conforme TXT.  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2021%3A2%3A46.png?version=1&modificationDate=1466290600000&api=v2)  
  
Resultado final  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2021%3A3%3A37.png?version=1&modificationDate=1466290651000&api=v2)  
   
Após confirmação da apuração de ICMS e geração do arquivo SPEDFISCAL com pergunta Wizard Gera registros DIFAL (EC 87/15) = Sim  
  
Será gerado registro E311.
