---
content_hash: d1d3d0b8e14969e3e5361c04ea915dc7cd7ded64712788f400ebe179c0555aec
fetched_at: '2026-06-29T00:11:11.422996+00:00'
page_id: '64652401'
product: rm
source: tdn-rm
title: NF-e - Desconto condicional
type: documentation
url: https://tdn.totvs.com/display/LRM/NF-e+-+Desconto+condicional
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Desconto condicional |
| **Subprocesso** | **:** | Desconto condicional |
| **Data da publicação** | **:** | 03/07/2013 |

**Introdução:**

As instruções deste documento é uma sugestão para preenchimento do campo Desconto Condicional, uma vez que o mesmo só é preenchido através de fórmulas. As regras específicas de cada cliente para concessão do desconto condicional devem ser observadas.

Essas instruções não se aplicam na integração com o Educacional, uma vez que os campos de descontos, tanto o condicional como o incondicional, são preenchidos através da Classificação de Bolsas.

**Objetivo:**

Auxiliar na parametrização correta para que o “Desconto Condicional ” tanto no movimento quanto no item sejam levados para o XML da NF-e.

**Criando a formula:**

Para criar a formula realize o seguinte procedimento: No RMNucleus vá em: Cadastros |Formulas | crie as seguintes formulas:

**Desconto Condicional para o Movimento**

Cod: DMC

TABMOV ('VALOREXTRA1' , 'V')

**Desconto Condicional para o Item**

Cod: DIC

TABITM ('RATEIOEXTRA1' , 'V')

**Editando o tipo de movimento:**

Após criar as formulas será necessário parametrizar o tipo de movimento para a utilização do desconto condicional. Para isso vá em Opções | Parâmetros | RMNucleus | localize o tipo de movimento desejado e edite-o. Vá à etapa Mov – Valores Financeiros 1/4 e Habilite o campo valor extra 1:

Em seguida vá em Mov – Valores Financeiros 2/4 e Informe as fórmula para calcular o desconto condicional no Movimento e no Item informando as fórmulas criadas anteriormente.

**Habilitando rateio proporcional:**

Ao utilizar desconto no movimento para que o mesmo seja levado para o XML é obrigatório que o mesmo seja rateado pelos itens podendo ser condicional (formula)o proporcional (quantidade de itens e valor). Na etapa Mov – Rateio valores financeiros 2/2.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
