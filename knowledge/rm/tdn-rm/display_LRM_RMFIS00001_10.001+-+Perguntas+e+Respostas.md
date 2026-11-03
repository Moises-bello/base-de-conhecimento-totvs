---
content_hash: 9ec0ae002d4862f3b802e00d059b6d9fee46e7f4334c34efc6fcdf11fef6c9f9
fetched_at: '2026-06-29T00:06:00.256472+00:00'
page_id: '195300182'
product: rm
source: tdn-rm
title: RMFIS00001_10.001 - Perguntas e Respostas
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_10.001+-+Perguntas+e+Respostas
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

## **Para Lucro Presumido é necessário cadastrar e parametrizar o Evento Tributário?**

Sim, será necessário cadastrar e parametrizar o evento tributário. Para auxilio verifique: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventoLucroPresumidoArbitrado.aspx>

## **É necessário ter um evento tributário para cada período de apuração?**

Não, é possível possuir apenas um evento tributário para o período de apuração. Ao encerrar o período de apuração o Sistema irá verificar se há cadastro de Vigência do Evento Tributário. Para mais informações verifique: <http://tdn.totvs.com/pages/releaseview.action?pageId=189304598>

## **Ao criar o evento tributário a filial SCP não é apresentada.**

Os tributos da filial SCP devem ser apurados à parte dos tributos do sócio ostensivo. Para cada filial SCP será necessário fazer uma nova parametrização para geração da ECF diretamente na filial SCP. De acordo com o guia prático da rotina “caso a pessoa jurídica tenha Sociedades em Conta de Participação (SCP), cada SCP deverá preencher e transmitir sua própria ECF, utilizando o CNPJ da pessoa jurídica que é sócia ostensiva e o CNPJ/Código de cada SCP.”

## **É possível parametrizar o evento tributário por filial para que não seja considerado uma determinada filial que não participa do cálculo do imposto?**

Não é possível excluir uma única filial do cálculo do tributo. Entretanto, filtrar os lançamentos contábeis de uma única filial é possível. Para isso, basta marcar a opção “Regras por filial”, na aba Identificação do Evento Tributário. Com este campo marcado, o campo “Filial” ficará disponível para edição dentro do Item Tributário.

**Atenção!** Os tributos federais devem ser apurados de forma centralizada pelo estabelecimento matriz da empresa de acordo com as orientações da Receita Federal.

## **Quando tenho dois eventos tributários, um para Estimativa e outro para Balancete de Suspensão, como o sistema entende qual deles utilizar no encerramento do período de apuração?**

Ao encerrar o período de apuração o sistema irá buscar no Cadastro de Vigências que compreende o período que está sendo encerrado o Evento Tributário vigente para realizar a apuração.

## **É necessário utilizar os eventos tributários para geração da ECF?**

Sim. Para correta geração da ECF é imprescindível que os períodos de apuração do IRPJ e CSLL estejam encerrados e para apuração desses tributos o sistema exige Evento Tributário vigente para o período.

Para auxílio na parametrização dos eventos tributários verifique o link: <http://tdn.totvs.com/pages/releaseview.action?pageId=189304598>

## **Está disponível alguma documentação para a configuração dos eventos tributários e as amarrações com os períodos fiscais?**

Sim, verifique a documentação do TDN <http://tdn.totvs.com/pages/releaseview.action?pageId=189304598>.

## **Como vincular as contas contábeis nos grupos do Evento Tributário, pois tivemos muitas dificuldades.**

O Plano de Contas da empresa deve estar estruturado de forma que seja possível identificar cada um dos fatos inerentes à apuração do tributo. A parametrização do Evento deve ser supervisionada pela pessoa responsável pela área fiscal/tributária da empresa, para que a apuração do tributo seja realizada de forma correta.

## **Regras quando optarmos pelo "contábil" e na conta tiver ajuste que não deverá ser considerado, porém só tenho opção de débito, crédito, movimento... como proceder?**

Existem duas opções:

1. Utilizar as opções de filtro dentro de Item Tributário. São eles: Filial, Centro de Custo, Departamento, Histórico Padrão e Contas Gerenciais.
2. Se a primeira opção não for suficiente, utilize a opção do “Lançamento Manual” disponível no Anexo do Evento Tributário.

## **Nessa versão o processo de evento tributário está atendendo ao lucro da exploração?**

Ainda não. Mas, já está especificado e será desenvolvido em breve. Até lá, utilize a opção de Lançamento Manual para fazer a dedução do imposto. Os registros referentes ao Lucro da Exploração devem ser preenchidos manualmente no PVA.
