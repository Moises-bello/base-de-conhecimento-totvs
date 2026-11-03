---
content_hash: 1d04fd6c7ce330df23c01006dad61846f2715d1ed6fca343d21d272dd60c20fc
fetched_at: '2026-06-29T00:10:39.099395+00:00'
page_id: '546245211'
product: rm
source: tdn-rm
title: Cálculo de INSS para Múltiplos Vínculos no eSocial - Emenda Constitucional
  103/2019.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546245211
version: 9
---

A TOTVS trabalha para adequar os seus sistemas de folha de pagamento às regras das Emendas Constitucionais, Portarias e Notas Orientativas do eSocial.

Porém em alguns momentos as informações fornecidas pelos órgãos responsáveis são bastantes escassas, e acabam não contemplando diversos cenários existentes nos ambientes de nossos clientes.

Diante disso, informamos que referente às mudanças da [Nota Orientativa do eSocial 20/2019](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas-e-producao-restrita) e da atualização da [FAQ do eSocial (item 07.21)](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas-e-producao-restrita), onde relata sobre o cálculo de **INSS de trabalhadores com múltiplos vínculos,** estamos liberando uma primeira entrega para os clientes até o dia 17/04/2020, porém ainda não contempla 100% dos cenários adequados, pois estamos aguardamos as atualizações no ambiente do eSocial para que nossas implementações sejam validadas no ambiente do governo.

Ressaltamos que a atualização no ambiente de homologação do eSocial a partir da [Nota Técnica 17/2019](https://portal.esocial.gov.br/noticias/nota-tecnica-17-2019-disponivel-no-ambiente-de-testes) não foi realizada em tempo hábil, para que contemplássemos toda nossa gama de validações.

Perante este cenário e com o intuito em auxiliar nossos usuários na conferência da apuração dos encargos, relacionamos abaixo quais os processos que envolvem cálculos de encargos para múltiplos vínculos e quando aplicável, o mecanismo para identificação de possíveis diferenças que podem ocorrer.

Atenção!

Para mais detalhes sobre a forma de cálculo para múltiplos vínculos, acesse a documentação: 

**Importante:**Entende-se por múltiplos vínculos aqueles que trabalham para dois ou mais empregadores constituídos sob raiz de CNPJ’s diferentes.

  

**Cenários possíveis:**

1. **Trabalhador presta serviços a somente um empregador**: cálculo de encargos de INSS contemplado de acordo aos critérios de apuração do eSocial;
2. **Trabalhador presta serviços a mais de dois empregadores:** cálculo de encargos de INSS contemplado de acordo aos critérios de apuração do eSocial (acatará o que está informado nos eventos transmitidos ao ambiente do governo):

***Importante:*** *Até a competência abril/2020, o eSocial apenas efetuará o cálculo da contribuição descontada do segurado que prestar serviço em até dois empregadores simultaneamente (o declarante mais um). Nos demais casos (mais de dois empregadores simultâneos), o eSocial considerará como contribuição do segurado o valor efetivamente descontado e informado pelo empregador declarante. Esse procedimento visa a permitir aos empregadores a adequação dos seus sistemas internos ao novo modelo da tabela progressiva.*

       3.   **Trabalhador presta serviços a dois empregadores:** Nesta situação serão necessárias duas frentes para equalizar os valores de INSS descontados dos funcionários:

Com relação ao eSocial, caso ocorram divergências de valores, são duas as opções:

*Opção 1:*  Utilizar o DARF Avulso

Efetuar a geração e pagamento dos encargos através de DARF Avulso.

*Opção 2:* Manutenção de informações de múltiplos vínculos

Após geração do cálculo pelo roteiro de Múltiplos Vínculos:

Caso as duas empresas com raízes de CNPJ diferentes estejam cadastradas e enviadas ao TAF deve acessar o cadastro de eventos periódicos no TAF e realizar as alterações de forma manual.

Na primeira empresa em que é feito o cálculo do INSS, informar o CNPJ da outra empresa, o valor de Outras bases e o IndMV correto.

Desta forma, ao receber os eventos o eSocial fará o cálculo considerando a Nota Orientativa 20/2020.

## Exemplo:

Cálculo da folha

 

Retorno 5001 - Informações a previdência

1) Empregador A: R$ 602,04

É o primeiro a descontar. Não deve informar o grupo {infoMV}.

A tributação será:

- Remuneração: Categoria 101=  602,04

- 1ª Faixa: 602,04 x 7,5% = 45,15

**Contribuição descontada: 45,15** (categoria 101).

2) Empregador B: R$ 1.701,59

É o segundo a descontar. Deve informar no registro {remunOutEmpr} apenas o empregador ordenado antes dele, no caso o Empregador A (R$ 602,04). Informar indMV=[2].

A tributação será:

- Remuneração: Categoria 101= 1701,59

- Remuneração já tributada em outras empresas: 602,04( parte da 1ª Faixa já tributada na categoria 101)

- 1ª Faixa: (1.045,00 - 602,04) x 7,5% = 33,22 , e

- 2ª Faixa: (2.089,60 – 1.045,00) = 1.044,60 x 9% = 94,01, e

- 3ª Faixa: (2.303,63 - 2.089,60) = 214,03 x 12% = 25,68

**Contribuição descontada: 152,91** (categoria 101)

**- Contribuição Total somando empresas A e B = 198,06. (conforme Sistema Protheus)**

Atenção!

Para que a folha de pagamento realize o cálculo corretamente dos descontos de INSS de múltiplos vínculos em coligadas diferentes, é imprescindível respeitar a ordem para o cálculo. Exemplo: Empregador 1 deverá realizar o lançamento e calcular todos os valores referentes ao pagamento do seu vínculo para aquela competência, apenas após esse processo, o Empregador 2 poderá dar o início aos seus lançamentos e cálculos. Caso seja necessário realizar alterações no Empregador 1, sugerimos que seja feito o cancelamento dos lançamentos e feitos novamente na ordem que deseja enviar as informações ao governo.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.25 |
| 12.1.26 |
| 12.1.27 |
| 12.1.18 |

falsefalse

**Status:** Finalizado
