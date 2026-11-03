---
article_id: 1500009296382
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 303fc25783265b9c193819811ee0048bc2fbb8247d745f2b16cbe4073854274b
fetched_at: '2026-06-28T22:40:52.701201+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Como preencher
  os parâmetros para geração da ECD?
type: support-article
updated_at: '2024-01-25T13:51:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009296382-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Como-preencher-os-par%C3%A2metros-para-gera%C3%A7%C3%A3o-da-ECD
---

**Dúvida**Central de escrituração, como preencher os parâmetros/wizard para geração da ECD?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Contabilidade Gerencial - Todas as versões  
  
**Solução**

Menu Padrão: Atualizações + Escrituração Contábil + Central de Escrituração (CTBS001)

Posicione na opção ECD + botão incluir

**![ecdgeral.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016408041/ecdgeral.gif)**

**1) Tipo Escrituração?**

1.Com centralização:  
As tabelas de MOVIMENTOS contábil (exemplo CT2, CQ0,CQ1..) podem ser exclusivas ou compartilhadas, porém só será permitido selecionar uma filial por vez.

2. Sem centralização (Descentralizada- Gera o registro 0020)  
Caso as tabelas de movimentos sejam exclusivas por filial (CT2,CQ0,CQ1..) e as tabelas de cadastro compartilhadas (CT1, CTT, CTS) poderá ser selecionado mais de uma filial, com a obrigatoriedade de informar a matriz consolidadora.   
Nesta opção os Demonstrativos (DRE, BP...) e lançamentos serão aglutinados em um único TXT.  
No Registro 0000 irá conter o CNPJ da consolidadora e no Registro 0020 o CNPJ das filiais.

**Importante!**  
Entrega consolidada e plano de contas diferente (tabelas de cadastros)?  
Deverá ser criado no SIGAMAT uma filial consolidadora e processar a rotina CTBA231 –Consolidação configurada (Plano de contas diferente)

Plano de contas iguais (tabela de cadastro) mas não quer gerar o registro 0020?  
Deverá ser criado no SIGAMAT uma filial consolidadora e processar a rotina  
CTBA220- Consolidação Geral.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125892-MP-SIGACTB-ECF-e-ECD-Centraliza%C3%A7%C3%A3o-e-descentralizada>

**2) Situação Especial?**

* Calendário contábil ( rotina CTBA010) deve conter exatamente o período da situação especial.
* Caso não seja uma situação especial informar Z- Normal.

Apuração anual, o calendário contábil deve ser mensal contendo o ano inteiro.

Apuração trimestral, calendário trimestral, contendo os 4 trimestres do ano.

obs. Caso não tenha um calendário contábil nesse formato, deverá ser cadastrado um novo calendário  sem amarração de moeda e informa-lo na wizard da ECD.

**3) Indicador Início de Período?**

Informe a opção 0- Inicio no primeiro dia do ano.

Caso a escrituração não inicie no primeiro dia do ano informe:

1- Abertura

2- Resultado Cisão/Fusão ou Remanescente

3- Início de obrigatoriedade ECD

**4) Indicador de existência de NIRE:**

0- Empresa não possui NIRE  ou

1- Empresa possui NIRE.

Caso a empresa possua NIRE, deverá possuir essa informação no SIGAMAT.

Configurador (SIGACFG) + ambiente + empresas + filial.

Na aba Adicionais, informar o campo e a data do NIRE.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017326181/mceclip0.png)

Na ECD o NIRE esta localizado no registro I030 campo 7:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017061902/mceclip1.png)

Obs: Data do Arquivamento dos Atos Constitutivos: É a data de arquivamento do ato de  
constituição da empresa. As datas de alterações contratuais devem ser desconsideradas. Em termos práticos, é a data do NIRE. Para empresas que não possuem NIRE, será considerada a data de abertura da empresa.

Data de Arquivamento do Ato de Conversão de Sociedade Simples em Sociedade Empresária: É a data em que a Junta Comercial arquivou o documento que formaliza a conversão. Em termos práticos, é a data do NIRE.

**5) Indicador de finalidade da escrituração?**

0- Original

1- substituta.

Caso seja uma escrituração substituta, deverá ser gerado o registro J801 (Termo de Verificação para Fins de Substituição da ECD) conforme documentação a seguir:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025353791-MP-SIGACTB-ECD-J801-SUBSTITUTA>

**6) Tipo da ECD (SCP)?**

Para gerar a ECD como Sócio Ostensivo ou como SCP siga para documentação:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007042511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Documenta%C3%A7%C3%A3o-SCP-e-S%C3%B3cio-Ostensivo>

**7) Plano Referencial?**

O plano de contas para ECD não é obrigatório, mas é aconselhável devido ao relacionamento e recuperação da ECF para transmissão da ECD.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022515312-MP-SIGACTB-ECD-COMO-GERAR-OS-REGISTROS-I050-E-I051-PLANO-DE-CONTAS-E-PLANO-DE-CONTAS-REFERENCIAL>

**8) Moeda Funcional diferente da Nacional?**

As pessoas jurídicas obrigadas a transmitir, via Sped, a escrituração em moeda funcional diferente da moeda nacional, nos termos do art. 156 da Instrução Normativa RFB no 1.515, de 24 de novembro de 2014, deverão preencher o campo identificação de moeda funcional do registro 0000 (0000.IDENT\_MF) com “S” (Sim)

Quanto 0000.IDENT\_MF for igual a “S”, os campos já existentes nos registros I155, I157, I200, I250, I310 e I355 deverão ser preenchidos com os valores baseados em moeda funcional, atendendo ao disposto nos artigos 155 e 156 da Instrução Normativa RFB no 1.515/2014. Consequentemente, os valores do bloco J serão verificados pelo programa da ECD, por meio dos códigos de aglutinação, considerando os valores baseados em moeda funcional dos registros do bloco I.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025045771-MP-SIGACTB-ECD-MOEDA-FUNCIONAL>

**9) Escrituração contábeis consolidada?**

Bloco k- Conglomerados Econômicos

Deverão preencher este bloco as empresas controladoras obrigadas a apresentar demonstrações consolidadas de acordo com a legislação societária (Lei no 6.404/76 e/ou Pronunciamento Técnico CPC 36 – Demonstrações Consolidadas).

Em caso de ECD normal, só poderá haver informação de escriturações contábeis consolidadas quando o período da ECD contiver o mês ou fração do mês de dezembro.

Ao informar "SIM" deverá ser relacionado o cadastro do conglomerado na pergunta a seguir:

**Código Bloco K?**

Criação do relacionamento do conglomerado:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050375913-MP-SIGACTB-ECD-Gera%C3%A7%C3%A3o-do-Bloco-K->

**10) Ocorreu mudança no plano de contas?**

Se a resposta é "SIM" deverá ser gerado o registro I157

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003409082-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-gerar-o-registro-I157-da-ECD->

**11) Existe amarração com Plano Referencial?**

Se a resposta for "Sim" deverá haver amarração na tabela CVD (plano de contas x plano de contas referencial) para geração do registro I051, conforme documentação:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022515312-MP-SIGACTB-ECD-COMO-GERAR-OS-REGISTROS-I050-E-I051-PLANO-DE-CONTAS-E-PLANO-DE-CONTAS-REFERENCIAL?source=search>

**12) Outras inscrições?**

Neste registro, devem ser incluídas as inscrições cadastrais da pessoa jurídica que, legalmente, tenha direito de acesso ao livro contábil digital. O código da empresa no Banco Central corresponde ao “ID\_Bacen”, conforme registrado no Unicad (Informações sobre Entidades de Interesse do Banco Central), composto por 8 dígitos e iniciados com a letra "Z".

**13) Indicação da escrituração?**

Todos os livros da escrituração contábil podem ser incluídos no Sped Contábil, em suas diversas formas.  
São previstas as seguintes formas de escrituração:  
• G - Diário Geral;  
• R - Diário com Escrituração Resumida (vinculado à livro auxiliar);  
• A - Diário Auxiliar;

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024645212-MP-SIGACTB-ECD-LIVRO-A-DI%C3%81RIO-AUXILIAR>

• Z - Razão Auxiliar;

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025044871-MP-SIGACTB-ECD-COMO-GERAR-O-LIVRO-Z-Layout-parametriz%C3%A1vel->

• B - Livro de Balancetes Diários e Balanços;

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026160292-MP-SIGACTB-ECD-REGISTRO-I300-e-I310->

Como gerar o Livro A ou Z (Registro I015)

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025836991-MP-SIGACTB-ECD-REGISTRO-I015-LIVRO-A-ou-Z>

Como gerar o Livro R ou B (Registro I015)

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025836551-MP-SIGACTB-ECD-REGISTRO-I015-LIVRO-R-OU-B>

Como gerar o livro Z (Registro I012)

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023272831-MP-SIGACTB-ECD-LIVRO-Z-REGISTRO-I012>

**14) Número de ordem do livro?**

É o número do livro. A numeração dos livros é sequencial, por tipo de livro, independentemente de sua forma (em papel, fichas ou digital). Assim, se o livro anterior, em papel, é o 50, o próximo (digital ou não) é o 51.

Os livros Diários (G e R) devem ter a mesma sequência numérica.  
Os Diários Auxiliares devem ter numeração própria, sequencial, por espécie, assim como o livro Razão Auxiliar. Assim, se foram utilizados "Diário Auxiliar de Fornecedores" e "Diário Auxiliar de Clientes", cada um terá uma sequência distinta

**15) Natureza do livro?**

Corresponde à denominação do livro (nome do livro). Normalmente, os livros G e R recebem o mesmo nome, sendo os mais comuns “Diário” e “Diário Geral”. Os nomes mais comuns de livros auxiliares são: “Diário Auxiliar de .....”, “Razão Auxiliar de .....”, “Livro Caixa” ou “Livro de Inventário”.

**16) Período inicial lcto?**  
**Período Final Lcto?**

Deverá deve conter exatamente o período da escrituração que o arquivo txt será composto.

Regra geral, a ECD será entregue em apenas um arquivo correspondente a todo o ano-calendário, podendo ser entregue em arquivos com períodos mensais, ou contendo vários meses (ex.: trimestral).  
Os períodos de escrituração do livro principal e dos livros auxiliares devem coincidir. Portanto, se a escrituração possui um livro principal e um livro auxiliar e, em virtude do tamanho, o livro principal é fracionado em 12 livros mensais, o livro auxiliar também deverá ser dividido em 12 livros mensais, seguindo os períodos adotados no livro principal.

Existem outros limites:

- Todos os meses devem estar contidos no mesmo ano.  
- Não deve conter fração de mês (exceto nos casos de início de atividade, cisão parcial ou total, fusão,  
incorporação ou extinção).

**17) Apuração do exercício (L/P)?**

Na ECD será o campo [DT-EX-SOCIAL,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025075131-MP-SIGACTB-ECD-CAMPO-OBRIGAT%C3%93RIO-N%C3%83O-PREENCHIDO-DT-EX-SOCIAL-) Deverá ser preenchido com data de 31/12/XX para empresas que possuem apuração ANUAL ou para empresas TRIMESTRAIS que irão gerar o arquivo "Trimestral UNIFICADO" ou seja, os 4 trimestres em um TXT (vide pergunta 23).

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025075131-MP-SIGACTB-ECD-CAMPO-OBRIGAT%C3%93RIO-N%C3%83O-PREENCHIDO-DT-EX-SOCIAL->

**18) Calendário?**

O calendário contábil é responsável em gerar o registro I150 (Saldos Periódicos )

O calendário contábil (CTBA010) deve conter exatamente o período contábil.

* Apuração anual, o calendário contábil deve ser mensal contendo o ano inteiro (12 períodos)
* Apuração trimestral, calendário trimestral, contendo os 4 trimestres do ano.

obs. Caso não tenha um calendário contábil nesse formato, deverá ser cadastrado um novo calendário  sem amarração de moeda e informa-lo na wizard da ECD.

**19) Moeda?**

Moeda forte utilizada para contabilização em moeda REAL.

**20) Tipo Saldo (Societario)?**

Tipo de saldo utilizado para atender a contabilização societária.

**21) Conta De?**  
**Conta Ate?**

Deve ser informado o range de contas do plano de contas.

Lembrando que só não serão exportadas contas SEM SALDO/MOVIMENTO.

Sendo assim, Caso a conta esteja bloqueada mas tenha saldo anterior e/ou movimento no período, a conta será gerada.

Caso esteja gerando com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search) e o centro de custo tenha saldo anterior e/ou movimento no período a conta também será gerada.

**22) Plano Contas Referencial?**

Informar o plano referencial que possui amarração para contas analíticas (tabela CVD), destinado a escrituração.

**23) Arquivo Trimestral Unificado?**

Arquivo trimestral Unificado? SIM

Deverá:

* Realizar a apuração de resultado trimestralmente
* Possuir o Calendário Contábil trimestral  (caso possua um calendário anual, deve incluir um calendário trimestral sem amarração da moeda rotina CTBA010).

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025347591-MP-SIGACTB-ECD-A-PARTIR-DO-LAYOUT-7-TRIMESTRAL-UNIFICADA->

**24) Período Inicial Demons?**  
**Período Final Demons?**

Deve conter o período correspondente a escrituração.

**25) Cod. Cof Bal. Patrim?**  
**Cod.COnf. DRE?**

Como gerar J100 (Balanço Patrimonial):

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Registro-J100>

Como Gerar o J150 (DRE):

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-COMO-GERAR-O-REGISTRO-J150->

**26) Processo C. Custo?**

Se irá gerar com Centro de Custo:

https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search

**27) J210: Indicador do tipo de demonstração?**

Informe o DLPA ou DMPL

**28) J210: Cod conf.Dem?**

Informe a visão gerencial:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026412372-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Como-gerar-DMPL-ou-DLPA-na-ECD-Registros-J210-e-J215->

**28) J215**

Caso informe o J210, será necessário detalhar o fato contábil.

Facilitador de detalhamento:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018715631-MP-SIGACTB-ECD-Facilitador-ECD-DMPL-Recupere-os-registros-J200-e-J215-de-uma-revis%C3%A3o-anterior>

**29) J800 (Notas explicativas).**

Caso seja necessário enviar uma nota explicativa, seguir os procedimentos a seguir:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025129432-MP-SIGACTB-ECD-J800-A-PARTIR-DO-LAYOUT-7-COMO-GERAR-NOTA-EXPLICATIVA>

**Saiba mais:**

Razão Auxiliar das subcontas (RAS)

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025045491-MP-SIGACTB-ECD-LIVRO-Z-RAZAO-AUXILIAR-DAS-SUBCONTAS-RAS->

Tipos de livro Z

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025045971-MP-SIGACTB-ECD-TIPOS-DE-LIVRO-Z->
