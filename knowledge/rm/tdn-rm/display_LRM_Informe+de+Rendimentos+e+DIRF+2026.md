---
content_hash: c6024782f5584a2f2af46ef45bfe308d1eee3aa4d8086a7968271d940986016e
fetched_at: '2026-06-29T00:05:47.458678+00:00'
page_id: '1014658015'
product: rm
source: tdn-rm
title: Informe de Rendimentos e DIRF 2026
type: documentation
url: https://tdn.totvs.com/display/LRM/Informe+de+Rendimentos+e+DIRF+2026
version: 45
---

Seja bem-vindo(a) à nossa página dedicada aos processos e etapas para a **Geração do Informe de Rendimentos e DIRF 2026** (Ano-Base 2025) na Folha de Pagamento do RM.

**Nosso objetivo** com esta página centralizadora é garantir que você tenha acesso rápido e descomplicado ás informações necessárias para conferir e **gerar corretamente** o Informe de Rendimentos e DIRF 2026.

1true1Informe de RendimentosInforme de Rendimentos

## **01. Qual é o pré-requisito para gerar o Informe de Rendimentos 2026 (Ano-Base 2025)?**

Para que o informe seja gerado, é obrigatório marcar os parâmetros:

* + Deletar Ano de Referência
  + Atualizar dados Informe de Rendimentos – RM Portal

## **02. O produto sofrerá melhorias para o Informe de Rendimentos de 2026?**

Sim. Iremos realizar algumas tratativas no menu Anuais | DIRF/Informe de Rendimentos, sendo elas:

1 – Desabilitar alguns parâmetros no Informe de Rendimentos (ano > 2024). Quando o ano informado for superior a 2024, manter desabilitados os parâmetros:

* Usa filtro de seleção ao gerar DIRF em Arquivo
* Utiliza descrição da seção selecionada na DIRF em Arquivo  
  (ambos os paramentos não se aplicam mais após o fim da DIRF)

2 – Adequar a tabela PDIRF para geração no Portal. Como o Informe de Rendimentos do Portal depende da tabela PDIRF, será necessário habilitar os parâmetros:

* Deletar Ano de Referência
* Atualizar dados Informe de Rendimentos – RM Portal

3 – Adequar  o quadro "Campo 4 - Rend. Isentos e não Tribut."  disponibilizando a  aba "Juros de mora recebidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função".

## **03. É necessária a atualização de algum patch?**

No momento não, pois não haverá alterações na geração do Informe de Rendimentos por parte do produto. As mudanças previstas referem-se apenas à usabilidade de telas conforme mencionado no item 02 acima.   
Dessa forma, não é obrigatória a atualização do patch para a geração do Informe de Rendimentos.

No entanto, caso o governo publique alguma alteração que exija adequações no produto, os ajustes necessários serão realizados e disponibilizados nasreleases de mercado 12.1.2502, 12.1.2506, 12.1.2510 e posteriores.

## **04. Qual o prazo de entrega do Informe de Rendimentos?**

O prazo é 27 de fevereiro de 2026.

## **05. Passo a passo para geração do Informe de Rendimentos?**

* Geração do Informe de Rendimentos através do menu Anuais | DIRF/Informe de Rendimentos.
* A conferência poderá ser realizada de duas formas:
  + Relatório de conferência de IRRF (Painel de Conferência de IRRF)
    - [Middleware - Relatório de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=782303914)
    - [TAF - Painel de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=781873283)
  + Ficha Financeira.

**ATENÇÃO:** A geração doInforme de Rendimentos utiliza exclusivamente as informações apuradas no **cálculo da Folha de Pagamento**, ou seja, **não busca informações no retorno do evento S-5002**.

## **06. Alteração da data entrega do informe de rendimentos?**

* Liberada tratativa no campo **"Data da Entrega"** para a geração do Informe de Rendimentos.
* [DT - Informe de Rendimentos 2026 - Tratativa no campo "Data da Entrega"](https://tdn.totvs.com/pages/viewpage.action?pageId=1041790426)

2DIRF Ano Base 2025DIRF Ano Base 2025

## **01. VISÃO GERAL**

Declaração do Imposto sobre a Renda Retido na Fonte (DIRF) não será mais utilizada. A nova forma de prestação de informações está estruturada em dois pilares principais:

* **eSocial:** sistema responsável pelo recebimento das informações trabalhistas e previdenciárias, inclusive as relativas à folha de pagamento. Por meio dessa ferramenta, são declarados os rendimentos pagos a empregados, contribuições previdenciárias, FGTS, impostos retidos e demais obrigações relacionadas aos vínculos empregatícios. Também devem ser informados no eSocial os rendimentos pagos a pessoas físicas sem vínculo empregatício, quando relacionados a atividades de trabalho, como no caso de prestadores de serviços autônomos.
* **EFD-Reinf:** a Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais (EFD-Reinf) é destinada à prestação de informações relativas a pagamentos realizados a pessoas jurídicas e a pessoas físicas e retenções de tributos, além de outras informações relativas a contribuições sociais.

A substituição da DIRF elimina a duplicidade de informações e torna o processo mais eficiente, alinhado à modernização promovida pelo Sistema Público de Escrituração Digital (SPED). Com isso, a Receita Federal "aposenta a DIRF" após décadas de relevantes "serviços prestados" e adota um modelo mais moderno para o cumprimento das obrigações tributárias.

É fundamental que os empregadores assegurem o correto preenchimento e envio das informações ao eSocial e à EFD-Reinf. Isso garante a conformidade fiscal, evita inconsistências e assegura que os contribuintes pessoas físicas recebam corretamente a declaração pré-preenchida do Imposto de Renda.

## **02. MELHORIAS  DISPONIBILIZADAS**

Para deixar os objetivos das rotinas mais claro, iremos realizar algumas tratativas no menu Anuais | DIRF/Informe de Rendimentos, sendo elas:

1 -Mensagem é exibida no inicio do processo DIRF/Informe de Rendimentos:

2 – É apresentada uma mensagem ao selecionar “DIRF Conferência” ou “DIRF em Arquivo” para ano base > 2024, exibindo alerta quando o usuário informar ano superior a 2024.

3 - Banner na fila de eventos.

## **03.****AÇÕES NECESSÁRIAS**

A principal ação é a **conferência e parametrização correta das rubricas** 

1. **Atualização do Sistema:** Garanta que seu sistema esteja na versão mais recente, compatível com o leiaute **S-1.3 do eSocial**.
2. **Parametrização de Rubricas:** Verifique se todas as rubricas de pagamentos, descontos e informativos estão com a **incidência tributária do Imposto de Renda Retido na Fonte (IRRF) correta**. Is
3. **Evento S-1210 (Pagamentos):** Este evento foi ampliado para detalhar as informações necessárias à substituição da DIRF. É crucial que ele contenha todos os dados fiscais relevantes, incluindo informações de plano de saúde coletivo e previdência privada.
4. **Conferência Mensal:** O departamento pessoal deve realizar a conferência mensal dos valores no eSocial, comparando com os relatórios gerados pelo produto. Isso permite a verificação de erros e acertos em paralelo.

* + As conferências poderão ser feitas através de 3 tipos de relatórios:
    - Relatório de conferência de IRRF (Painel de Conferência de IRRF)
      * [Middleware - Relatório de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=782303914)
      * [TAF - Painel de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=781873283)
    - Relatório de Conferência de IRRF S-5002 -
    - Ficha Financeira.

## **DEMAIS INFORMAÇÕES**

* [Fim da DIRF X eSocial](https://www.youtube.com/watch?v=f7hzXfAqMkg)
* [DT - Informe de Rendimentos 2026 - Juros de mora recebidos pelo atraso no pagamento](https://tdn.totvs.com/display/LRM/DT+-+Informe+de+Rendimentos+2026+-+Juros+de+mora+recebidos+pelo+atraso+no+pagamento)

* [Middleware - Relatório de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=782303914)
* [TAF - Painel de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=781873283)
