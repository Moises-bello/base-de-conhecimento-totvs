---
content_hash: b261aaa02647e22e37ae2d81dd37f6ab007d040634501e1faea7e361e6c2b6e8
fetched_at: '2026-06-29T00:11:16.280862+00:00'
page_id: '66618323'
product: rm
source: tdn-rm
title: RMFIS00021_Parametrização F500 - Lucro Presumido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66618323
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | EFD Contribuições – Lucro Presumido |
| **Subprocesso** | **:** | Parametrização do Processo para geração do registro F500/F525 |
| **Data da publicação** | **:** | 11/07/2013 |

**Definição do Processo**

---

* **É imprescindível ter o sistema TOTVS Gestão Financeira(RM Fluxus) instalado e parametrizado no ambiente de geração.**

Este “Como Fazer” tem por objetivo, auxiliar na parametrização do **TOTVS** **Gestão** **Fiscal** (**RM** **Liber**), para geração do registro **F500** na rotina Federal **EFD** **Contribuições** **(Lucro Presumido)**. Os registros referentes à escrituração do **PIS/Pasep** e da Cofins das pessoas jurídicas sujeitas ao regime de tributação com base no lucro presumido, aplicável para os fatos geradores a ocorrer a partir de 01 de julho de 2012, serão disponibilizados pelo Programa Validador e Assinador (PVA) da **EFD Contribuições**, versão 2.01, com previsão de disponibilização pela Receita Federal em Junho/2012.

A empresa tributada pelo Lucro Presumido e que também se enquadre na incidência da contribuição previdenciária sobre a receita bruta, deve apresentar a **EFD** Contribuições a partir de março ou abril APENAS com as informações da contribuição previdenciária (Bloco P). As informações sobre a apuração do PIS e COFINS devem ser informadas a partir de julho de 2012.

As empresas estão dispensadas de entregar a **EFD** Contribuições nos meses que não auferiu receitas sujeitas ao pagamento das contribuições. No mês de Dezembro, entretanto, deve ser entrega a **EFD**informando os meses do ano calendário em que não auferiu receitas no Registro 0120.

As empresas tributadas com base no Lucro Presumido devem informar apenas as operações representativas de receitas, nos seguintes moldes:

**• Escrituração pelo Regime de Caixa: Registros F500**;

**• Escrituração pelo Regime de Competência: Registros F550 ou**

**• Escrituração pelo Regime de Competência: Escrituração detalhada, com base nos Registros dos Blocos “A”, “C”, “D” e “F”.**

As informações para geração dos registros consolidados no Regime Caixa serão buscadas no sistema de **Gestão Financeira**, de acordo com as considerações abaixo. Ainda para o Regime de Caixa, devem ser gerados os Registros:

**• 1900 – Consolidação dos documentos emitidos no período**

**• F525 – Demonstração da origem da receita recebida.**

A escrituração pelo Regime de Competência de forma consolidada através do Registro F550 não será gerada pela Linha RM.

A geração da **EFD Contribuições** de forma detalhada seguirá o processo já existente, gerado para as empresas tributadas pelo **Lucro Real**.

**Parametrizações Necessárias**

---

**1. Versões Necessárias**

Para configuração deste processo é necessário:

**• Versão RM LIBER: 11.40.5(50) ou superior**

**2. Parametrização do Processo EFD Contribuições – Registro F500**

---

Foi criado um Processo (Opções | Parâmetros | Processos), semelhante ao Processo existente hoje para geração do F100, vinculado, também, à Tabela de Tipo de Documento. Neste Processo deverão ser  
informados todos os Tipos de Documentos utilizados pela empresa para registrar suas operações de receita.

Na tela de inserção do Tipo de Documento será apresentado o campo “Tipo de Documento” para preenchimento pelo usuário. Para cada Tipo de Documento informado, devem ser informados, também, os  
tributos e seus respectivos CSTs.

A partir da versão “11.40.05.072 [ TOTVS Gestão Fiscal ]”(ou superior) (disponível no nosso site de Downloads), será disponível ao usuário escolher qual campo, do lançamento financeiro, será carregado  
para o Valor da Base de calculo dos tributos PIS/COFINS:

**IMPORTANTE**: A seleção dos lançamentos continua sendo feita a partir da **Data de Baixa** no sistema Financeiro e as informações geradas nos Registros **F500** e filhos.

**3. Cálculo dos Docs. Não Escriturados**

Após a parametrização do Processo do Registro F500, assim como é feito na geração do registro F100 para Lucro Real, é necessário executar o Cálculo dos DOcs. Não Escriturados através do Menu  
Utilitários | Gerador de Saídas | Cálculo das Contribuições Docs Não Escriturados

**Esta função realiza o seguinte cálculo:**

São selecionados lançamentos (à receber) Financeiros **(RM FLUXUS)** que tenham o mesmo tipo de Documento que foi Configurado no Processo do **RM LIBER**. Estes lançamentos devem estar baixados  
dentro do período de seleção que foi escolhido na tela acima.

**Lançamentos baixados a partir de créditos**

Os lançamentos financeiros baixados a partir de "Nota de crédito" e\ou "Adiantamento de crédito" também tem os tributos PIS\COFINS preenchidos após a execução do processo de "Cálculo dos Docs não Escriturados" e serão considerados na geração do Lucro Presumido.

**Exemplo Prático:**

**a)** Inserido lançamento Financeiro a receber com Tipo de Documento **“F500”** no de Valor Original de R$999,00, na aba Valores Tributos, veja que ainda não foi informado pelo **“Cálculo dos DOcs. Não Escriturados”** o PIS/COFINS informados no processo do RM LIBER:

**b)** Baixar o lançamento Financeiro:

**c)** Informações gravadas no Lançamento Financeiro:

Veja que o Valor Original esta com R$999,00 e o Valor Baixado com R$952,55, como a Base de calculo informada no processo esta “Valor Original”, os tributos serão inseridos com Base de Calculo = Valor Original, no caso R$999,00.

**4. Tela de geração da rotina**

Foi implementado, na tela de geração da EFD Contribuições, um parâmetro para que o usuário informe o Regime adotado para o Lucro Presumido com as seguintes opções:

**• Regime de Caixa.**

**• Regime de Competência - Escrituração Detalhada.**

Se o usuário informar a opção “Regime de Competência - Escrituração Detalhada” o sistema vai gerar o arquivo de acordo com as regras atuais, utilizada pelas empresas tributadas pelo Lucro Real. O Campo 05 - IND\_REG\_CUM do Registro 0110 será preenchido com a informação “9 – Regime de Competência - Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F””.

Se o usuário informar a opção “Regime de Caixa” o sistema irá buscar o Processo parametrizado para a seleção dos lançamentos financeiros:

• A seleção dos lançamentos será pela Data de Baixa e o Campo 05 - IND\_REG\_CUM do Registro 0110 será preenchido com a informação “1 – Regime de Caixa – Escrituração consolidada (Registro F500)”.

**Arquivo Gerado:**

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/Fis.EFDLucroPresumido.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
