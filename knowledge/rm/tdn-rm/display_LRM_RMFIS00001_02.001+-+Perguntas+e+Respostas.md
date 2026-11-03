---
content_hash: 4fff7c24f79c5893d8a41b892e0eef2ed20a50c0d23c6e2823cd94817e68fbe9
fetched_at: '2026-06-29T00:06:00.223067+00:00'
page_id: '195300013'
product: rm
source: tdn-rm
title: RMFIS00001_02.001 - Perguntas e Respostas
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_02.001+-+Perguntas+e+Respostas
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

## **As abordagens do Workshop referente à ECF servirão para toda a linha de produtos da TOTVS?**

Não, o Workshop abordou apenas informações para a Linha RM.

**A versão do RM 12.1.4 contempla a geração da ECF?**

Não. A geração da rotina ECF para a versão 12.1 está disponível na versão 12.1.5 ou superior.

**Importante:** Na versão 12.1 não é necessário a execução do script (ExecSql.RMLIBER.ECF.TotvsScript.zip). Lembrando que para correta geração da ECF é necessário que o Sistema e layout da rotina estejam atualizados de acordo com a última versão disponível no Portal do Cliente – Download e Atualizações (<https://suporte.totvs.com/download>).

## **A versão 11.82 contempla a geração da ECF?**

Sim, a geração da ECF na versão 11.82 está disponível na versão 11.82.38 ou superior.

**Importante:** Para correta geração da ECF é necessário que o Sistema e layout da rotina estejam atualizados de acordo com a última versão disponível no Portal do Cliente – Download e Atualizações (<https://suporte.totvs.com/download>)

## **Onde encontro todas as informações sobre a geração da ECF?**

Toda a documentação para auxílio na geração da ECF está disponível no TDN - <http://tdn.totvs.com/pages/releaseview.action?pageId=187828905>

## **Para quem iniciará a parametrização do sistema para geração da ECF seria ideal iniciar pelos eventos tributários?**

Para quem vai partir do zero indicamos acompanhar o passo a passo do TDN, link: (<http://tdn.totvs.com/pages/viewpage.action?pageId=187828905>)

## **A geração da ECF está disponível apenas na Nova MDI?**

Não, a geração da ECF está disponível na Nova MDI e no executável RM Liber.

## **Para geração da ECF é necessário adquirir o RM Liber?**

Sim, para geração da ECF é imprescindível o acesso ao Totvs Gestão Fiscal.

## **Os dados para geração dos registros da rotina ECF serão informados manualmente no sistema?**

A geração da ECF pela Linha RM busca, automaticamente, informações contábeis e as informações da apuração dos tributos IRPJ e CSLL desde que corretamente parametrizados.

## **Como habilitar a opção ECF no sistema?**

Para habilitar a opção ECF acesse o aplicativo RM Liber:  Rotinas Legais | Rotinas Federais | ECF (Opção 04.03.15 – ECF), e libere a permissão. Não esqueça de ajustar o Perfil de segurança dos usuários que irão trabalhar com a rotina.

## **Caso a opção ECF não apareça no menu Rotinas Federais, pode estar faltando executar algum script?**

Sim, será necessário verificar se o Script ExecSql.RMLIBER.ECF.TotvsScript.zip foi executado sem erros e se o sistema está corretamente atualizado para a verão 11.82.38 ou superior.

**Lembre-se**: na versão 12.1 NÃO é necessária a execução do script.

## **Na Integração Entre Sistemas é obrigatório marcar a integração entre todos os sistemas\coligadas?**

Para fins da ECF, é necessário habilitar a integração “RM Saldus x RM Liber” para que as informações contábeis sejam geradas. No mais, as integrações são definidas na implantação do sistema, de acordo com os processos da empresa.

## **Para geração da ECF obrigatoriamente tem que ter o Saldus e o Liber integrados?**

Não, porém caso o Saldus não esteja integrado com o Liber não serão gerados os blocos/registros de informações provenientes da contabilidade, por exemplo, Blocos J (Plano de Contas e Referenciamento) e K (Saldos contábeis).

## **Será necessário utilizar o processo de escrituração de Movimentos do RM Nucleus para o RM Liber?**

Não, a geração da ECF será realizada a partir das informações do RM Saldos, através das contas contábeis parametrizadas no Evento Tributário.

## **Onde que é feito a parametrização da rotina Escrituração Contábil Fiscal?**

A parametrização para geração da ECF é feita em: Cadastros | Filial | Anexos | Parâmetros – ECF.

Para auxílio na parametrização acesse: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.AnexoFilialParametrosECF.aspx>

## **O encerramento do período foi realizado antes da atualização do sistema para geração da ECF, será necessário reabrir os períodos para as configurações da rotina?**

Sim, será necessário abrir os períodos de apuração, ajustar a parametrização dos Eventos Tributários no que for preciso. Depois disso, os períodos de apuração devem ser encerrados novamente.

## **Existem empresas que não recolhem CSLL por ter conseguido esse direito por decisão judicial. Elas terão problemas na geração da ECF?**

Não, para empresas que não recolhem o CSLL não será apresentado erro ao gerar a rotina.

## **O sistema oferece algum recurso para migrar a DRE versão Delphi e eventos tributários ou será cadastrado tudo novamente?**

A DRE deve ser criada na nova ferramenta de Demonstrações Contábeis.

Para mais informações consulte o link: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.DemonstracaoContabil.aspx>

Já os eventos tributários dos tributos IRPJ e CSLL que já foram criados em Delphi foram migrados para a nova plataforma, assim não será necessário cadastrar as informações novamente apenas ajustar com as novas informações solicitadas.

## **Onde que eu posso verificar as integrações do sistema?**

Para verificar as integrações do sistema acesse: TOTVS Gestão Fiscal | Ambiente | Parâmetros | Integrações Entre Sistemas.

## **Há alguma particularidade a ser observada pelas Entidades Sem Fins Lucrativos que devem ser observadas?**

Com relação à operacionalização do sistema não. Entretanto, em caso de dúvida com a obrigação em si, sugerimos que a entidade consulte seus especialistas em tributação.

## **O cadastro do PAT e de Prejuízos Fiscais que existiam na apuração do IRPJ ainda precisa ser cadastrada?**

O antigo cadastro de Compensação do PAT e da Compensação de Prejuízo/Base Negativa foram desativados. Estão disponíveis no sistema apenas para consulta. Esses valores agora devem ser controlados no Lalur – Parte B.

## **Tem como disponibilizar o manual completo do RM Liber, pois temos este sistema mas não está parametrizado.**

Sim, toda documentação do aplicativo RM Liber está disponibilizada no Help do Sistema (Ajuda | Conteúdo | Menus RM Liber), no Wikehelp (<http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Liber.aspx>) e TDN (<http://tdn.totvs.com/pages/releaseview.action?pageId=4812112>).
