---
article_id: 34900857950615
category: Escrita Fiscal - Configurador de Tributos
content_hash: 78508e38a6d00fd76874325e2b3b77c158080da30199f022a108be3aece353c2
fetched_at: '2026-06-28T22:39:17.729475+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Campos
  da TES irá permanecer com a implantação do Configurador de Tributos.
type: support-article
updated_at: '2026-06-23T14:43:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34900857950615-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Campos-da-TES-ir%C3%A1-permanecer-com-a-implanta%C3%A7%C3%A3o-do-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34900857937303) Tempo aproximado para leitura: 00:10min  
  
**Dúvida**  
Quais campos da TES irá permanecer com a implantação do Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir do release **12.1.2510**  
  
**Solução**  
Este documento visa contribuir para o entendimento dos clientes sobre o processo de transição dos cálculos do tributos pelo Tipos de Entrada e Saída (**MATA080**) para o **Configurador de Tributos (FISA170)**.  
  
Nosso planejamento prevê a migração completa de todas as operações fiscais para o Configurador de Tributos até 2027.  
  
E para apoiar essa transição, abaixo lista os campos do cadastro de Tipos de Entrada e Saída (**MATA080**) que permanecerão ativos com a exclusiva função de **integração entre os módulos**.

A migração para o Configurador de Tributos é essencial para modernizar a gestão tributária, garantir a conformidade fiscal e introduzir novos tributos, melhorando a eficiência operacional.

![](https://tdn.totvs.com/download/attachments/928965724/image-2026-3-10_16-35-19.png?version=1&modificationDate=1773171322597&api=v2)

##### **CAMPOS QUE PERMANECEM NO TES**

| F4\_FILIAL | Filial |
| --- | --- |
| F4\_CODIGO | Cod. do Tipo |
| F4\_TIPO | Tipo do TES |
| F4\_DUPLIC | Gera Dupl. |
| F4\_ESTOQUE | Atu.Estoque |
| F4\_EFUTUR | Entrega Futura |
| F4\_CF | Cod. Fiscal |
| F4\_TEXTO | Txt Padrao |
| F4\_PODER3 | Poder Terc. |
| F4\_UPRC | Atu.Pr.Compr |
| F4\_CONSUMO | Mat.Consumo |
| F4\_CIAP | L.Fisc. CIAP |
| F4\_ATUATF | Atual.Ativo |
| F4\_TESDV | Tes Devol. |
| F4\_TESP3 | Tes Ret.Simb |
| F4\_QTDZERO | Qtd.Zerada |
| F4\_SLDNPT | Sld.Poder 3 |
| F4\_DEVZERO | Custo Dev. |
| F4\_TIPOPER | Tipo Operac. |
| F4\_MSBLQL | Bloqueado |
| F4\_TESENV | TES P/envios |
| F4\_FINALID | Finalidade |
| F4\_TRANFIL | Trans filial |
| F4\_BENSATF | Desme.IT.ATF |
| F4\_TESE3 | Tes Rem.Simb |
| F4\_TEMDOCS | Possui Docs |
| F4\_PAGCOM | Pg. Comissao |
| F4\_CODPAG | C. Pagamento |
| F4\_VLRZERO | Vlr. Zerado |
| F4\_IDHIST | ID Hist. |
| F4\_TRANSIT | Trf.transito |
| F4\_CONTERC | Amz. Terc.? |
| F4\_COMPONE | Bem Componente |
| F4\_CIAPTRB | Tributa CIAP |
| F4\_CFPS | Código Fiscal de Prestação de Serviço |
| F4\_OPEMOV | Operacao de Movimento |
| F4\_AJUSTE | Ajuste CIAP |
| F4\_ATUTEC | Atualiza SigaTec |
| F4\_NATOPNF | Natureza operação NFS-e |
| F4\_BONIF | Entrada de bonificação? |
| F4\_MOVFIS | Movimentação Física |
| F4\_BENSATF | Desmembra Itens no ativo. |
| F4\_CODBCC | Cod.BC Cred. PIS/COFINS |
| F4\_DESPPIS | Desp. Acessória PIS |
| F4\_DESPCOF | Desp. Acessória COFINS |
| F4\_PSCFST | PIS/COF ST |
| F4\_CSTPIS | CST PIS |
| F4\_CSTCOF | CST COFINS |
| F4\_MALQPIS | Alíquota PIS Majorada |
| F4\_MALQCOF | Alíquota COFINS Majorada |
| F4\_TNATREC | Tabela Natureza Receita PIS/COFINS |
| F4\_CNATREC | Código Natureza Receita PIS/COFINS |
| F4\_GRPNATR | Grupo Natureza Receita PIS/COFINS |
| F4\_DTFIMNT | Data Fim Nat. Receita PIS/COFINS |
| F4\_CSTPF1 | CST PIS F100 |
| F4\_CSTCF1 | CST COFINS F100 |
| F4\_EFDF100 | Gera F100 EFD Contribuições |
| F4\_PISCOF | Calcula PIS/COFINS |
| F4\_PISCRED | Credita PIS/COFINS |
| F4\_BASEPIS | Redução Base PIS |
| F4\_BASECOF | Redução Base COFINS |
| F4\_PISDSZF | Desconto PIS Zona Franca |
| F4\_COFDSZF | Desconto COFINS Zona Franca |
| F4\_INTBSIC | PIS/COFINS Importação |
| F4\_AGRPIS | Agrega PIS |
| F4\_AGRCOF | Agrega COFINS |
| F4\_MSGLT | Mensagem do Lote |
|

Documentações relacionadas:

[CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12)

[FAQ – Descontinuação das operações fiscais da TES e adoção do Configurador de Tributos](https://tdn.totvs.com/pages/releaseview.action?pageId=923184811)
