---
content_hash: 86b667824ab2b9dbb0ed02f07aad77b61e7ac656cdab12aeff1d70ebad360d44
fetched_at: '2026-06-29T00:05:56.601137+00:00'
page_id: '152802651'
product: rm
source: tdn-rm
title: RMFIS00001_Rotinas Estaduais - Como gerar Gia do RJ
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_Rotinas+Estaduais+-+Como+gerar+Gia+do+RJ
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:**11.50/11.80 |
| **Processo** | **:** | Rotinas Estaduais - GIA RJ |
| **Subprocesso** | **:** | Como gerar a rotina Gia do Rio de Janeiro |
| **Data da publicação** | **:** | 22/08/2014 |

***Definição do Processo***

O objetivo deste documento é oferecer uma visão geral a respeito da geração da GIA RJ.

**Introdução**

De acordo com a RESOLUÇÃO SEF N.º 6.410 DE 26 DE MARÇO DE 2002, **Art. 1.º** A Guia de Informação e Apuração do ICMS (GIA-ICMS) é a declaração mensal que se destina à demonstração do imposto apurado pelo contribuinte em cada período e à apresentação de outras informações de interesse econômico-fiscal.

**Gerando a Rotina**

Acesse: Rotinas Legais | Rotinas Estaduais | Apuração de ICMS | Informe o Estado Rio de Janeiro e a Rotina GIA.

Na tela de geração da rotina será informado:

- O **nome do Arquivo** que será gerado pelo Sistema. **OBS:** O nome sugerido pela Norma de Procedimento é GIARJ.TXT;

- A **Filial** que o arquivo será gerado;

-A **Referência**, que será o Período de geração do arquivo;

- A **Versão** atual do Layout da GIA ICMS pré-estabelecido pela SEFCON;

- Caso o arquivo gerado seja retificador deverá ser marcado o Flag **Declaração Retificadora,** caso o arquivo seja normal o Flag deverá ficar desmarcado;

- As informações do campo **Observação** será utilizada no registro 0110;

- No campo **Observação ST** deverá ser preenchido com informações referentes às Operações com Substituição Tributária. Essas informações serão utilizadas no registro 0110.

Na aba Outros Dados da tela de geração da rotina será informado:

- Informe se a Filial de geração do arquivo **Possui Movimentações no Período do Tipo** Operações Próprias, Substituição Tributária, Outros ICMS, ALZ / Zona Franca Manaus, para isso marque ou não os flags.

OBS: As informações relativas às operações com Substituição Tributária não estão sendo geradas pelo sistema.

 - No campo Destino será marcado o destino para geração do arquivo, caso seja marcado drive C: será considerado o caminho indicado em Opções | Parâmetros | Gerais Tabelas | Rotinas legais | Dir. Aq. Temporário.  
 - **Gerar Relatório Espelho** e **Gerar Relatório Resumo Espelho:** marcando esse flag após a geração da rotina será apresentado os relatórios com as informações que foram geradas para o arquivo texto da Gia par conferência.

**Informações Adicionais:**

- Para geração do registro 0230 deverá ser utilizado nos lançamentos de saída com tipo de tributação ICMS Isento, lembrando que a opção ALC/ZFM na aba Outros Dados da tela de geração da rotina deverá ser marcada.

- Os seguintes registros não são gerados pelo sistema:

**0190 –** Movimentação de Operações com Prazo Especial

**0240 –** Movimentação de SCE Compensado entre Estabelecimentos

**0250 –** Movimentação de SCE Compensado do Próprio

**0260 –** Movimentação de SCE Recebido

**0270 –** Movimentação de SCE Transferido

- Para mais informações sobre a geração e registros da Gia acesse o Help do Sistema, Ajuda | Conteúdo | Menus RM Liber | Rotinas Legais |Rotinas Estaduais | Apuração ICMS | Rio de Janeiro | GIA.

Para maiores informações:

Icon

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoINSS.aspx)

**COMUNIDADE **[R@Fiscal](http://fluig.totvs.com/portal/p/10097/subject/rfiscal)****

**Canais de Atendimento:**

**Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
