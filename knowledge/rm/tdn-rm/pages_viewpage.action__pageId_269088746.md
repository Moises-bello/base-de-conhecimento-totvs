---
content_hash: 8672cd115e3ee07d69319e65f271202654ec54f6d0d445dce72706f93611c188
fetched_at: '2026-06-29T00:08:22.259376+00:00'
page_id: '269088746'
product: rm
source: tdn-rm
title: 208857_Geração_Movimento_Caixa_Calculo_ValorLiquido_Customizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269088746
version: 142
---

# Geração de Movimento (regime de caixa)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Movimento* | *Geração de Movimento* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *.* |  | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** | MEDU-1270 / MEDU-1243 |
| **Requisito (ISSUE):** |  |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

O módulo de geração de movimento no TOTVS Gestão Educacional possibilita, via parametrização, que o valor do item de movimento possa ser composto da seguinte forma:

**Valor original**

Para esta opção o sistema vai gerar no valor do item do movimento o valor original do lançamento financeiro, e os valores referente a desconto de bolsa (exceto bolsa condicional) e de parcela serão gerados no campo desconto.

**Valor líquido**

Para esta opção o sistema vai gerar somente o valor do item do movimento, considerando o valor original do lançamento - valores de desconto de bolsa (exceto bolsa condicional) - descontos parcelas. O campo desconto do item de moviemnto não será preenchido, pois o valor do item já está abatido os descontos.

**Cenário não contemplado**

Alguns clientes parametrizam descontos através de campos de valores opcionais que compõem o lançamento financeiro, e estes valores são calculados por fórmula sem nenhuma relação com o educacional.

Esses descontos podem ser dedutíveis na base de cálculo e devem ser considerados ao gerar o movimento pelo educacional.

**Evolução**

Com objetivo de flexibilizar a parametrização de composição do valor do item de movimento iremos realizar uma evolução na parametrização deste recurso permitindo ao cliente parametrizar uma fórmula que será responsável por calcular o valor líquido (baseado no lançamento financeiro), e que irá compor o valor do item do movimento.

Não poderíamos fixar este valor como sendo o valor liquido disponível no lançamento financeiro uma vez que podemos ter valores de descontos considerados no lançamento financeiro que **são ou não** **dedutíveis,** cabendo ao cliente determinar tal regra.

**Regras**

**Parametrização:**

Educacional >> Integração >> Fiscal

1. Campo “Valor item do movimento”:  a opção "Valor líquido" terá sua descrição alterada para "Valor líquido educacional"
2. Campo “Valor item do movimento”:  será adicionada mais uma opção “**Valor líquido ( calculado por fórmula )**”.
3. A nova opção disponibilizada no primeiro item somente ficará disponível ou poderá ser selecionada se a opção “Utilizar movimento por competência” estiver desmarcada, ou seja, este **recurso poderá ser utilizado somente por clientes que geram movimento em regime de caixa**.
4. Ao selecionar a opção “**Valor líquido ( calculado por fórmula )**” serão habilitados dois campos para que o usuário parametrize as fórmulas que serão utilizadas para calcular o valor líquido que irá compor o valor do item de movimento.  
     
   Campo 1 - Fórmula de cálculo do valor a ser executada para lançamentos em aberto e parcialmente baixados**.**  
   **Está formula será executada sobre o contexto do lançamento financeiro (FLAN)**Campo 2 - Fórmula de cálculo do valor a ser executada para lançamentos baixados.  
   **Está formula será executada sobre o contexto dos itens de baixa do lançamento (FLANBAIXA)**  
     
   **Observações:**  
   - O contexto de execução das fórmulas será o lançamento financeiro vinculado à parcela ou o item de baixa do mesmo, e neste caso as fórmulas a serem utilizadas deverão ser criadas no módulo TOTVS Gestão Financeira e depois parametrizadas no TOTVS Gestão Educacional.

**Geração de Movimento**

1. Para lançamentos parcialmente baixados o sistema executará a fórmula de lançamento ("Campo 1") e não a fórmula de lançamentos baixados, pois por estar parcialmente baixado, os valores de baixa que podem ser processados não estariam corretos.
2. Se a fórmula a ser executada sobre lançamentos baixados não estiver parametrizada (“Campo 2”), o sistema executará a fórmula parametrizada para lançamentos em aberto ("Campo 1").
3. Para lançamentos totalmente baixados e que foi parametrizada uma fórmula no (“Campo 2”), o sistema irá executar a fórmula sobre todos os itens de baixa do lançamento acumulando o resultado da execução. Isto se faz necessário, pois podemos ter lançamentos totalmente baixados com vários itens baixa.
4. O valor processado pela execução da fórmula irá compor o valor do item do movimento representado como valor líquido, portanto o valor de desconto no item de movimento não será preenchido.
5. Se na tela do processo de geração de movimento a opção “Gerar movimentos para boletos de valor líquido igual a zero” estiver marcada, o sistema permitirá a geração de movimentos em que a fórmula executada retorne valor igual a zero.
6. Será apresentado no LOG do processo o valor processado pela fórmula conforme o movimento gerado.
7. Será adicionado na tabela SPARCELAMOV o campo "ORIGEMVLRITEMMOV". Este campo armazenará a informação que identifica se o valor foi calculado pelo Educacional ou Fórmula.
8. Na geração do movimento iremos validar se o valor retornado pela fórmula parametrizada, violou a regra de descontos concedidos no educacional

   **Regra**: O valor líquido calculado pela fórmula não pode ser maior que o valor líquido calculado pelo educacional.

                Valor líquido educacional = Valor parcela - descontos de bolsa incondicional - descontos de parcela.

   Por exemplo:  
   Valor parcela: 1000,00  
   Bolsa incondicional: (10%) 100,00  
   Desconto Parcela: (5%) 50,00  
   ----------------------------------------------------------------------  
   Valor líquido educacional: 850,00  
   Valor líquido retornado pela fórmula: 900,00  
     
   Observe no exemplo que conforme a fórmula executada o desconto seria apenas de 100,00 e que no educacional o desconto corresponde à 150,00, neste caso os valores processados pela fórmula violaram os descontos concedidos pelo educacional.

   | Atenção  Ressaltamos alguns pontos importantes que devem ser observados na utilização deste recurso:  1. Mesmo que o valor líquido seja calculado por fórmula todas as parametrizações referentes a descontos de bolsa que impactam ou não na geração do movimento devem ser mantidos para que a regra do item 8 seja aplicada. 2. Como o recurso de calcular o valor líquido por fórmula é totalmente codificado pelo cliente, destacamos alguns cenários que devem ser observados na codificação da fórmula (levando em consideração se o cliente trabalha com os recursos destacados), tais como:  - O lançamento financeiro pode contemplar valores aproveitados da conta corrente do aluno  - O lançamento financeiro pode estar baixado parcialmente 3. Valores de descontos do lançamento financeiro podem estar parametrizados para serem calculados por fórmulas e, quando o lançamento estiver em aberto e utilizarmos a função de fórmula “VALORLIQUIDO” , as fórmulas dos campos de descontos levarão em consideração a data de execução na geração do movimento e acreditamos que isso possa impactar no cálculo do valor liquido. Cabe ao cliente avaliar o cenário e adequar as fórmulas. 4. **O processo de geração de movimento sempre gera um único movimento para cada lançamento, mesmo se o lançamento for baixado parcialmente, ou seja, se após várias baixas do lançamento for solicitada a geração de um movimento para um lançamento que já tenha boletos com movimentos gerado, o sistema vai regerar o movimento já criado considerando as novas informações. O sistema não gera um movimento para cada boleto.** |
   | --- |

## Procedimentos para Configuração

Demonstração da parametrização para utilizar o recurso de cálculo do valor líquido por fórmula.

Importante!

As funções de fórmula utilizadas neste exemplo são ilustrativas, ressaltamos que as codificações destas fórmulas serão realizadas conforme as regras de cada cliente, sendo de total responsabilidade do cliente a forma como estes valores serão processados e irão compor o valor do item do movimento.

**CRIAÇÃO DAS FÓRMULAS**

1. No **RM,** acesse **Serviços Globais**/Fórmula**.** Crie/configure a(s) fórmula(s):

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **Educacional/Configurações/Parâmetros.** Configure em Integração/Fiscal/Fiscal 2/2 o parâmetro a seguir:

**EXECUÇÃO PROCESSO**

2.  No **RM,**acesse **Financeiro-Contábil/NF-e/Geração de Movimento** e execute o processo:

 

divs
