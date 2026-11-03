---
article_id: 360063097093
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: fe3893885622eff9f7977882bea46d4e6abe0a781082467d194e34122b81674d
fetched_at: '2026-06-28T22:40:48.920848+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS300/ TAFA331 Base
  de calculo para apuração e simulação do Lalur e diferença de saldos nos lançamentos
  exportados para o TAF
type: support-article
updated_at: '2023-08-01T14:33:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063097093-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS300-TAFA331-Base-de-calculo-para-apura%C3%A7%C3%A3o-e-simula%C3%A7%C3%A3o-do-Lalur-e-diferen%C3%A7a-de-saldos-nos-lan%C3%A7amentos-exportados-para-o-TAF
---

**Dúvida**CTBS300/TAFA331, Base de calculo para apuração e simulação do Lalur e diferença de saldos nos lançamentos exportados para o TAF  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80

**Solução:**

**Base de calculo:**

O TAF irá considerar como base de cálculo os lançamentos contábeis, conforme período, que estiverem na rotina TAFA331 (lançamento contábil).

**Passo 1**;

CTBS001 + EXPORTA ECF

Essa opção é necessária para que o plano de contas seja exportado e alimente a tabela C1O (plano de contas TAF).

**Mas atenção!** Se já possui plano de contas no TAF e não houve alteração e inclusão de conta contábil. Não é necessário realizar esse processo.

**Passo 2**;

 Cadastro Filtro Lalur-  Rotina [CTBS300.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015738232-MP-SIGACTB-CTBS300-ONDE-CADASTRAR-FILTRO-LALUR-?source=search)

Deve ser relacionado o range de contas de resultados e/ou patrimoniais e o centro de custo (caso utilize),

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15269286757015)

**Passo 3;**

Exportação Lalur- CTBS001,

No "exporta LALUR" serão exportar os lançamentos contábeis da rotina CTBA102 para a rotina TAFA331.

Perguntas:

* **Cod.Filtro Lalur?** = Busca o filtro da rotina CTBS300.
* **Data?** = Inicio e Fim
* **Moeda?** 01
* **Saldos?** 1
* **Processa C.Custo?**
* **Carga Saldo Inicial?** Só poderá ser feito uma vez e o sistema só irá considerar as contas patrimoniais, pois as contas de resultado são zeradas periodicamente. Essa carga inicial deve ser feita na implantação do LALUR e os saldos patrimoniais serão alimentados no ultimo dia do período anterior.
* **Extrai Movimentos?**Normal, extemporâneo ou ambos?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15269300984727)

Tabelas utilizadas:

Exportar os dados da CT2 para CSA e CSB 

Gera registro na TAFST1 e TAFS2 = T124 

* **Motivos para diferenças entre o SIGACTB e TAF**

**Ocorrência 1:**

Issue [DSERCTR1-33519](https://jiraproducao.totvs.com.br/browse/DSERCTR1-33519) (Criada 04/08/2021) No range de exportação com mais de 1 dia (ctbs001 + exporta lalur), o primeiro lançamento, dos dias seguintes, não são exportados para o TAF.

Como paliativo a exportação de um dia de cada vez, irá alimentar o TAF corretamente.

**Ocorrência 2:**

Caso tenha mais de um cadastro lalur (Cod.Filtro Lalur? = rotina CTBS300)

É importante saber que o tipo de lançamento não esta na chave de integração (T124). Por isso exportar o mesmo período, com os mesmo parâmetros (alterando somente o cadastro lalur campo Cod.Filtro Lalur?) irá sobrepor os lotes que o range de contas tem em comum.

Exemplo: Cadastro lalur 0001 conta 1010101001

                Cadastro lalur 0002 conta 4010101001

Note que os lançamentos no SIGACTB possuem a mesma data, lote, sublote e documento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405659211799)

Ao exportar o lalur com o código 0001 a integração é feita com um debito de 20.000,00 e um crédito de 100,00 porque no filtro tem apenas a conta 1010101001.

Se houver a exportação do lalur código 0002 para o mesmo período e parâmetros o sistema não irá complementar com o Debito e o Credito das contas de resultado, ele irá sobrepor o lote 0001.

Para ajustar essa situação deve-se criar um cadastro (ctbs300) abrangendo os 2 ranges de contas (0001 e 0002).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405665970839)

**Dúvidas frequentes:**

* É possível gerar somente o LALUR pelo sistema ou só é possível gerar se for fazer a ECF?

R: Para a apuração do LALUR só utilizamos da ECF o plano de contas, então se já possui plano de contas no TAF (tabela C1O) e não houve alteração e inclusão de conta contábil. Não é necessário exportar o ECF (ctbs001 + ecf) antes de exportar as movimentações para o lalur (ctbs001 + lalur).

Mas se é a primeira vez que esta gerando o ECF, ou esta em um ambiente novo ou mudou de plano de contas, é necessário exportar o ECF primeiro para que o plano de contas seja populado na tabela do TAF (C1O).

Os movimentos, saldos e valores do Lalur, não dependem da ECF para serem apurados. Após a apuração há possibilidade de exportar as fichas do LALUR para o bloco M e N da ECF, nesse caso, o ECF precisa ter sido exportado para o TAF pois a exportação do bloco M e N faz validação com o bloco K da ECF.

* Posso exportar mais de uma vez a opção "exporta lalur" no período?

R: Sim, a tabela de movimentos contábeis geralmente possui um volume muito grande de dados, sendo assim o "exporta Lalur" pode ser feito de forma diária, quinzenal, mensal... como preferir.

* A opção SEM CENTRALIZAÇÃO me permite exportar várias filiais de uma única vez, existe algum pré-requisito para funcionar corretamente?

R: Sim, Ao exportar SEM CENTRALIZAÇÃO, as tabelas de cadastro devem ser COMPARTILHADAS e as de movimento EXCLUSIVA. Esse procedimento é necessário pois os dados cadastrais que serão alimentados no TAF serão da MATRIZ se as filiais possuir um plano de contas diferente, por exemplo, ao exportar o ECF + LALUR as contas das filiais não serão encontradas pois o plano de contas é da Matriz.

**Importante** que a C1O e C1P (Plano de contas e centro de custo do TAF)  tenham o mesmo compartilhamento que a CT1 e CTT (Plano de contas e centro de custo SIGACTB), por exemplo.

*Compartilhamento SIGACTB: [Compartilhamento Tabelas SIGACTB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-)*

* Para que serve a Carga Inicial de Saldos?

Sabemos que a base de calculo do Lalur é baseada nas contas de resultados, porém conforme legislação vigente, algumas contas patrimoniais como de Provisões podem ser adicionar ou excluídas da base de calculo. São para esses casos que a carga de saldo inicial foi criada.

Essa carga inicial deve ser feita na implantação do LALUR e os saldos patrimoniais serão alimentados no ultimo dia do período anterior.

* No filtro do lalur (CTBS300) tenho contas de resultado e patrimoniais, posso exportar a carga inicial ou tenho que criar um filtro somente de contas patrimoniais?

R: Pode exportar a carga inicial com filtro de contas patrimoniais e de resultado sim. Como as contas de resultado foram zeradas no período anterior (CTBA211) o saldo delas não serão acumulado.

* O que são l*ançamentos extemporâneos*?

De acordo com o art. 6º-C da Instrução Normativa RFB nº 1.422/2013, no caso de lançamentos extemporâneos em ECD que alterem a base de cálculo do IRPJ ou da CSLL da ECF de ano calendário anterior, a pessoa jurídica deverá efetuar o ajuste por meio da apresentação de ECF retificadora relativa ao respectivo ano-calendário, mediante adições ou exclusões ao lucro líquido. Para isso, foram criadas linhas específicas nos registros M300 e M350.

Exemplos:

M300A – LINHA 91.40 - Ajustes de Exercícios Anteriores - Lançamentos Extemporâneos   
M300A – LINHA 166.35 - (-) Ajustes de Exercícios Anteriores - Lançamentos Extemporâneos   
M300A – LINHA 265.40 - Ajustes de Exercícios Anteriores - Lançamentos Extemporâneos   
M300A – LINHA 340.35 - (-) Ajustes de Exercícios Anteriores - Lançamentos Extemporâneos

Como gerar lançamentos extemporâneos: [Lançamentos Extemporâneos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025053772-MP-SIGACTB-ECD-COMO-GERAR-LAN%C3%87AMENTOS-EXTEMPOR%C3%82NEOS)

**Saiba mais**

Cadastro Evento tributário:  [Evento Tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404225269527-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Cadastro-do-Evento-tributario-BLOCO-M-e-BLOCO-N)
