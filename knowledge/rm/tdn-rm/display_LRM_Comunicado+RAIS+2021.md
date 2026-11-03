---
content_hash: f785014aee718b4dea650ae0266f74c809167b5e494335fa6e118f1c1641c6ff
fetched_at: '2026-06-29T00:10:58.093073+00:00'
page_id: '603124198'
product: rm
source: tdn-rm
title: Comunicado RAIS 2021
type: documentation
url: https://tdn.totvs.com/display/LRM/Comunicado+RAIS+2021
version: 36
---

O Ministério da Economia/Secretaria Especial de Previdência e Trabalho publicou os procedimentos para a declaração da Relação Anual de Informações Sociais (RAIS) - ANO BASE 2020 e disponibilizou o programa validador da **RAIS 2021** (GDRais 2020 - Versão 1.0.0), disponível em [www.rais.gov.br](http://www.rais.gov.br/) .

Para as empresas compreendidas nos grupos 1 e 2 do eSocial, conforme cronograma estabelecido pela Portaria 1.419/2019, estão DESOBRIGADAS a declarar a RAIS.

**O prazo legal de entrega da RAIS inicia-se em 13 de março de 2021 e encerra-se em 12 de abril de 2021, conforme [publicação](http://www.rais.gov.br/sitio/index.jsf.).**

As versões compatíveis com a RAIS 2021 encontram-se disponíveis para download em **[Portal Downloads e Atualizações](https://suporte.totvs.com/portal/p/10098/download#000023/12.1/CORPORE%20RM/).**

|  |  |
| --- | --- |
| **Versões:** | 12.1.28.267 ou Superiores  12.1.29.222 ou Superiores  12.1.31.125 ou Superiores |

O Manual de  orientação da RAIS Relação Anual de Informações Sociais (RAIS) - ANO BASE 2020, trouxe orientações sobre o preenchimento dos campos conforme layout:

Alterações de regras de preenchimento, conforme Manual Rais ano Base 2020:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Registro Tipo | POSIÇÃO | TAMANHO | TIPO | DESCRIÇÃO | ALTERAÇÃO |
| 0 | 393 a 584 | 192 | Alfanum | Espaços | Aumentou o tamanho. Antes eram 159 posições |
| 1 | 540 a 584 | 45 | Alfanum | Informação de uso exclusivo da empresa | Aumentou o tamanho de 12 para 45 |
| 2 | 544 a 573 | 30 | Alfanum | Matrícula | Inclusão do campo |
| 2 | 574 a 576 | 3 | Número | Categoria | Inclusão do campo |
| 2 | 577 a 584 | 8 | Alfanum | Informação de uso exclusivo da empresa | Alteração da posição do campo. Ele começava na posição 544 |
| 9 | 036 a 584 | 549 | Alfanum | Espaços | Aumentou o tamanho de 516 para 549 |

* **Declaração antecipada de encerramento das atividades:**Caso o estabelecimento tenha tido a baixa do seu cadastro no ano de 2020, mas aguardou o programa GDRAIS 2020, não precisa preencher o campo "encerramento de atividade".

* **Matrícula:**Informar a matrícula atribuída ao trabalhador pela empresa ou, no caso do servidor público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão. O preenchimento deste campo é OPCIONAL e deve-se observar a limitação de 30 (trinta) caracteres.

          **Atenção****:**Se o trabalhador tiver mais de um vínculo com o mesmo declarante, observadas as normas constitucionais de acumulação de cargos, empregos e funções públicas.

          Para cada vínculo deve ser atribuída uma matrícula. Havendo readmissão de emprego é considerado um novo vínculo e recebe uma nova matrícula.

* **Categoria:** O campo categoria foi incluído com o intuito de padronizar as informações da RAIS e do eSocial. Para o ano-base 2020, o preenchimento deste campo é OPCIONAL e deve conter o código da categoria do trabalhador, conforme a Tabela 01 do eSocial, disponível para consulta neste [link.](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-html/tabelas.html#01)

* **Motivos de afastamento do empregado/servidor durante o ano-base**: Incluído novo afastamento de código 85, que deve ser informado para os casos de Suspensão temporária do contrato de trabalho nos termos da Lei 14.020/2020 (conversão da MP 936/2020).

Verificar em Configurações | Parametrizador | 06.07-esocial | 06.07.02 - De/Para | De/Para de Afastamento a condição conforme o exemplo

Caso não exista a condição ou não atenda a condição acima, enviar o tipo de afastamento configurado no processo  Anuais|RAIS|Configuração de Afastamentos:

* **Dissídio**: Não podem ser incluídos os valores pagos referentes a exercícios anteriores, mesmo quando resultantes de dissídios coletivos, pagos a trabalhadores com contrato de trabalho vigente no ano-base a ser informado.

  *Exemplo*: dissídio coletivo para trabalhadores “ativos” na empresa, previsto para outubro de 2019, mas, devido à negociação sindical, os valores foram pagos em março de 2020. Os valores de dissídios referentes a janeiro a março/2020 serão declarados na RAIS ano-base 2020. Os demais valores, referentes a outubro, novembro e dezembro/2019, o estabelecimento deverá usar o programa GDRAIS Genérico 1976-2019), para corrigir essas informações, fazendo uma nova declaração de RAIS para os seus trabalhadores.

**Atenção:** Para atender a alteração acima, o produto de Folha de Pagamento passou a gerar as verbas de diferença por dissídio sempre no mês de referência, ou seja, nos casos em que houve pagamento de diferença salarial durante o ano, ao invés de levar para a remuneração os valores pagos apenas no mês, levará o valor correspondente em cada mês que teve a diferença calculada.

Com isso o parâmetro "**Gera Verbas de diferença por dissidio no mês de referencia"**dos parâmetros da coligada no processo de geração da RAIS foi retirado da tela a partir dos patches acima.

Nos casos em que houve pagamento de diferença salarial durante o ano, ao invés de levar para a remuneração os valores pagos apenas no mês, levará o valor correspondente em cada mês que teve a diferença calculada.

Lembrando que as verbas pagas por diferença de dissidio só serão levadas para os campos de remuneração mensal se a data de pagamento for igual ou anterior a data de demissão.

         

* **Lei 14.020/2020**: Para os trabalhadores que realizaram acordo de redução proporcional de jornada e de salário, com base na Lei 14.020/2020 (conversão da MP 936/2020), as remunerações mensais deverão ser declaradas de acordo com a folha de pagamento. Para os trabalhadores que realizaram acordo de suspensão temporária do contrato de trabalho, com base na Lei 14.020/2020 (conversão da MP 936/2020), não haverá indicação de remuneração mensal para os meses em que a suspensão compreendeu a competência integral do mês de referência. Caso a suspensão tenha sido parcial, as remunerações deverão ser declaradas de acordo com a folha de pagamento. Os trabalhadores que tiveram o contrato suspenso temporariamente nos termos da Lei 14.020/2020 (conversão da MP 936/2020), deverão ter as remunerações mensais informadas conforme folha de pagamento.

          **Atenção:**O sistema já valida a situação acima mencionada, abatendo o valor do evento descontado referente a MP 936 da remuneração, conforme sugerido na documentação da [MP 936](https://tdn.totvs.com/pages/viewpage.action?pageId=545621517).
