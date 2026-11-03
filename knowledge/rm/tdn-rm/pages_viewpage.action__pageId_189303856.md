---
content_hash: eb15206abe40663aaaf9667e8423fb32f3941d2c2c242ed6dc8a5a6860efe119
fetched_at: '2026-06-29T00:05:58.831535+00:00'
page_id: '189303856'
product: rm
source: tdn-rm
title: RMFIS00001_07.001 - Parâmetros Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189303856
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:**11.82.38/12.1.4 |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | Parâmetros Contábeis |
| **Data da publicação** | **:** | 25/05/2015 |

\**A geração da rotina ECF já está disponível na versão 12.1.5. IMPORTANTE: Na versão 12 não é necessário a execução do script (ExecSql.RMLIBER.ECF.TotvsScript.zip).*

A Escrituração Contábil Fiscal (ECF) substituiu a Declaração de Informações Econômico-Fiscais da Pessoa Jurídica (DIPJ), a partir do ano-calendário 2014. A rotina foi implementada no ambiente da 11.82.38 e da 12.1.5, últimas versões disponíveis.

O objetivo deste documento é oferecer orientações sobre os **Parâmetros Contábeis**, onde será possível definir opções de origem do TOTVS Gestão Contábil além de itens específicos do Regime de Apuração da empresa. A digitação destas informações é de inteira responsabilidade do Contribuinte devendo o mesmo solicitar auxílio de seu Contador ou Consultoria própria para o preenchimento deste Anexo.

**Parametrização Necessária**

---

Ao acessar o cadastro da Filial Matriz, em **Anexos | Parâmetros – Escrituração Contábil Fiscal**, é possível criar ou editar os parâmetros ECF. Na aba **Identificação** está disponível o menu: **Parâmetros Contábeis**. Clicando neste menu, o sistema exibirá a tela onde os dados serão pré-definidos.

A primeira informação necessária na parametrização, é verificar se o TOTVS Gestão Contábil está Integrado ao módulo TOTVS Gestão Fiscal. Quando esta opção estiver desmarcada o sistema entende que não existe integração com o Fiscal ou não fazem utilização do mesmo na empresa.

**Plano de contas Referencial**

Deverá ser vinculado o “Plano de Contas Referencial - ECD e ECF” disponível no site da Receita Federal ou na [Central de Download](https://suporte.totvs.com/download#0) com a descrição: **PLANOS\_REFERENCIAIS.ZIP**. Para importação deste Plano de Contas, siga as orientações contidas no artigo publicado no [TDN](http://tdn.totvs.com/display/public/rm/Plano+de+Contas+Referencial+-+Layout+3.0).

O item referente a parametrização do Plano de Contas Paralelo é obrigatório. Deverá ser informado o cadastro do plano de contas onde as contas referenciais se encontram devidamente vinculadas as contábeis, ou seja, informar o plano de contas referencial da instituição gestora, relacionado com as respectivas contas do plano de contas da Pessoa Jurídica. Somente devem ser referenciadas as contas analíticas com natureza de conta igual a 01 (contas de ativo), 02 (contas de passivo), 03 (patrimônio líquido) e 04 (contas de resultado). O Plano Referencial selecionado deve ser o mesmo utilizado na geração do SPED Contábil.

Documentação de Auxílio na utilização Transferência de Grupos Contábeis, [aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=65209087).

No regime do Lucro Real o usuário poderá optar pela forma de tributação com levantamento de balanço de suspensão/redução. Acesse o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.LucroReal.aspx) para ter orientações deste processo.

E para os demais regimes, siga a seguinte [Documentação](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.OutrasECF.aspx).

Para mais informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)

**COMUNIDADE **[R@Fiscal](http://fluig.totvs.com/portal/p/10097/subject/rfiscal)****

**Canais de Atendimento:**

**Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
