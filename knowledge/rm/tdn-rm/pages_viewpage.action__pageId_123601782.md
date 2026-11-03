---
content_hash: 08d0d85f83cfcf4af7528bf5e7a9c430118ffdd2fa4418b3c983e2103c8a504b
fetched_at: '2026-06-29T00:05:55.053702+00:00'
page_id: '123601782'
product: rm
source: tdn-rm
title: RMFIS00002_DIRF 2015 - Geração da rotina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=123601782
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.82.3x / 12.1.2 |
| **Processo** | **:** | DIRF - Declaração de Imposto de Renda Retido na Fonte |
| **Subprocesso** | **:** | Geração da rotina |
| **Data da publicação** | **:** | 02/02/2015 |

A DIRF - Declaração do Imposto Retido na Fonte é a declaração feita pela **FONTE PAGADORA**, Destinada a informar à Receita Federal o valor do Imposto de Renda Retido na Fonte, dos rendimentos pagos ou creditados durante o ano para seus beneficiários. No TOTVS Gestão Fiscal você consegue gerar as informações dos impostos retidos de pessoa jurídica e também os valores retidos pelo TOTVS Gestão Financeira.

**Parâmetros**

Acesse o parâmetro em **Opções | Parâmetros | Gerais / Tabelas | Rotinas Legais | Rotinas Federais | DIRF** e informe o diretório onde será criado o arquivo temporário da DIRF.

**Geração da Rotina**

Acesse a opção Rotinas Legais | Rotinas Federais | Declaração de Imposto de Renda – **DIRF**

Todas as informações devem ser preenchidas. O nome para o arquivo texto virá default como DIRF.TXT, mas é possível alterá-lo.

**Origem dos Dados**

**Buscar retenções lançadas no RM Fluxus**

Marque esta opção se deseja que o sistema selecione informações das retenções lançado no TOTVS Gestão Financeira. Marcando essa opção, as opções abaixo serão habilitadas:

**IRRF Pessoa Física – Autônomos**

O sistema seleciona informações dos Lançamentos de Retenção do imposto vinculados a códigos de Cli/For classificados como Pessoa Física.

**IRRF Pessoa Jurídica**

O sistema seleciona informações dos Lançamentos de Retenção do imposto vinculados a códigos de Cli/For classificados como Pessoa Jurídica.

 **Retenções das Contribuições Sociais**

O sistema seleciona informações dos Lançamentos de Retenções das Contribuições Sociais no sistema de Gestão Financeira.

**Observações**

Caso o Cliente optou por fazer a Apuração do Tributo IRRF (PJ) pelo RM Fluxus, não é necessário habilitar o Campo Busca IRRF PJ das retenções do RM Líber, pois isto gera erro de duplicidade.

**Retenções Lançadas no RM Liber**

**Busca IRRF PJ**

O sistema seleciona os lançamentos fiscais com destaque do Imposto “IRRF PJ” no Sistema de Gestão Fiscal (pasta Outros Tributos).

**Busca IRRF**

O sistema seleciona os lançamentos fiscais com destaque do Imposto IRRF lançados no Sistema de Gestão Fiscal.

***Atenção!*** *Habilitar esse parâmetro em conjunto com os parâmetros de “Buscar retenções lançadas no RM Fluxus” pode gerar duplicidade de informações!*

Buscar COSIRF

O sistema seleciona os lançamentos fiscais com destaque do imposto “COSIRF” no Sistema de Gestão Fiscal (pasta Outros Tributos).

**Buscar Contribuições Sociais**

O sistema seleciona os lançamentos fiscais com destaque das Contribuições Sociais no Sistema de Gestão Fiscal (pasta Outros Tributos).

***Atenção!*** *Habilitar esse parâmetro em conjunto com os parâmetros de “Buscar retenções lançadas no RM Fluxus” pode gerar duplicidade de informações!*

**Observações**

Serão considerados somente **os Lançamentos Fiscais de Entrada** com o Status diferente de Cancelado e Estornado.

Serão selecionados os Lançamentos Fiscais cuja Data do Lançamento esteja dentro do Ano Referência, definido na tela da rotina.

Se o lançamento deve ser selecionado na geração da Rotina, mesmo que não tenha retenção dos impostos, é necessário que sua base de cálculo e que o código da receita dos outros tributos estejam preenchidos.

**\*** Nas versões anteriores a 10.80 - As Retenções das Contribuições Sociais não serão selecionadas pela DIRF se forem informados no Sistema de Gestão Fiscal (RM Líber).

- O sistema passou a verificar se o CFOP dos lançamentos são do tipo “não fiscais”

- O sistema levará os lançamentos com os CFOP’s 1.933.XX e 2.933.XX independente se são fiscais ou não.  
Estas regras se aplicam para a composição da linha RTRT ( Rendimentos tributáveis).

**FLUXUS:**

Neste caso não houve mudanças na regra, somente correções referente à duplicidade de valor de dedução dos dependentes e o valor de Outras deduções (que não estava sendo levado para o campo de Pensão alimentícia).

**A principal mudança diz respeito à nova regra que diz que todos os Rendimentos do Cliente/Fornecedor devem ser considerados na linha do Rendimento Tributável (RTRT), desde que o mesmo tenha tido retenção em pelo menos um mês do período que estiver sendo gerado.**

**Outros Dados**

*Preencher conforme necessidade.*

**Observações para o Registro Tipo 2**

**Lançamentos Fiscais**

O campo Rendimentos Tributáveis é gerado com o valor da Base do Imposto, informado na Pasta Outros Tributos do Lançamento Fiscal. O campo Deduções é gerado zerado. O campo Imposto Retido é gerado com o valor do Imposto, informado na Pasta Outros Tributos do Lançamento Fiscal.

**Lançamentos Financeiros**

**1) IRRF**

O campo Rendimentos Tributáveis é gerado com o valor Original do Lançamento Financeiro.

Se houver redução da Base de Cálculo, o percentual de redução será considerado para efeito de cálculo deste campo. As deduções são geradas com o valor utilizado no cálculo deste imposto.Este campo é parametrizado no Cadastro do Cliente\Fornecedor – Pasta Dados Fiscais\Tributos.

**Observação**

A partir da versão 10.80.0 o valor das deduções por dependentes passou a ser detalhado nas colunas Dependentes e Pensão Alimentícia (Registro 02). O campo Imposto Retido é gerado com o valor do Imposto de Renda calculado para o Lançamento Financeiro

**2) Retenções das Contribuições**

**Atenção!** Habilitar esse parâmetro em conjunto com os parâmetros de “Buscar retenções lançadas no RM Liber” pode gerar duplicidade de informações!

O campo Rendimentos Tributáveis é gerado com o valor da Base de Cálculo informada na Pasta Outros Tributos, do Lançamento Financeiro Original.

O campo Deduções é gerado Zerado.

O campo Imposto Retido é gerado com o valor Original do Lançamento Financeiro cuja classificação se refere a Retenções das Contribuições Sociais.

**Dúvidas Frequentes**

**P: Ao gerar a Rotina da DIRF não estão sendo geradas as Retenções das Contribuições.**

**R**: o Fato gerador das Retenções (PIS, COFINS e CSLL) é o Pagamento do lançamento financeiro. Ao baixar o lançamento no TOTVS Gestão Financeira é gerado a DARF automaticamente, conforme a Parametrização do Cliente\Fornecedor.

**P: Como o Totvs Gestão de Pessoas gera um arquivo e o TOTVS Gestão Fiscal gera outro, como fazer a importação no programa da DIRF?**

**R**: Após fazer a importação do arquivo gerado pelo Totvs Gestão de Pessoas, é necessário fazer a importação do arquivo do TOTVS Gestão Fiscal, escolhendo a seguinte opção: Substituir pela soma dos dois.

O registro atual terá seus valores somados aos valores do registro que está sendo importado.

**P: Ao importar o arquivo da DIRF os lançamentos de Retenção PIS, Cofins e CSLL estão multiplicados.**

**R:** Isso pode ocorrer quando os Lançamentos que possuem retenção de PIS, Cofins e CSLL, tem tributos separados, mas com o mesmo código de Receita, gerando assim 3 guias diferentes. O código de Receita é utilizado para apurar os 3 Tributos (Pis, Cofins e CSLL) nas mesma guia. Caso a opção seja apurar os Tributos separados, cada um tem que ter o seu código de Receita.  
  
Para ajuste desta situação é necessário desfazer o processo: excluir as guias geradas, cancelar a baixa dos Lançamentos que geraram as Darfs, alterar o Código de Receita desses lançamentos e depois será necessário fazer todo o processo novamente, baixando os lançamentos e assim teremos as guias geradas corretamente.

**P: Não estão sendo levados alguns lançamentos de IRRF para a DIRF**

**R:** Para correta geração da DIRF, é obrigatória a geração das Guias pelo TOTVS Gestão Fiscal.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
