---
content_hash: 7de1b8115d4636ae0236fa4cd35aea579410531fbcf12559e687b6442d1977dc
fetched_at: '2026-06-29T00:09:20.531176+00:00'
page_id: '422545705'
product: rm
source: tdn-rm
title: Lucro Real Estimativa (Cálculo)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545705
version: 6
---

A entidade sendo tributada pelo Lucro Real, a pessoa jurídica pode apurar o lucro trimestralmente ou anualmente com pagamentos mensais apurados pelo Lucro Real - Estimativa.  
 ***Observação***: E imprescindível que a opção  "Cálculo Acumulativo" na identificação do Evento Tributário esteja marcada para a correta apuração pelo Lucro Estimado.

Na apresentação de pastas referente ao Lucro Real - Estimativa, será observada as seguintes regras:  
 **Opção "Levantamento de Balanço/Balancete de Suspensão / Redução"** - Desmarcada   
 **Estrutura de Pastas** - Habilitar as pastas conforme a forma de tributação Lucro Presumido

|  |  |
| --- | --- |
| **Tipo do Lucro** | **Apresentação de Abas** |
| **Lucro Real Estimativa** | Receita Bruta Alíquota 1  Alíquota 2  Alíquota 3  Alíquota 4  Demais Receitas  Exclusões da Receita  Adicionais do Tributo  Deduções do Tributo Compensação do Tributo |

Com o FLAG desmarcada as regras serão idênticas a do Lucro Presumido.

**Opção "Levantamento de Balanço/Balancete de Suspensão / Redução"** -Marcada  
 **Estrutura de Pastas** - Habilitar as pastas conforme a forma de tributação Lucro Real

|  |  |
| --- | --- |
| **Tipo do Lucro** | **Apresentação de Abas** |
| **Lucro Real** | Resultado Contábil  Adições do Lucro Adições por doação  Exclusões do Lucro  Compensação de Prejuízo Adicionais do Tributo Deduções do Tributo  Compensações do Tributo |

Com o flag marcado as regras serão idênticas a do Lucro Real e os ajustes não são registrados na Parte B do LALUR.

**Base de Cálculo Estimada**

Os percentuais sobre a receita bruta estimada, determinados de acordo com as atividades da entidade são: **1,6%**, **8%**, **16%** e **32%**.  
 No caso de atividades diferenciadas, deve ser aplicado o percentual correspondente sobre a receita originária de cada atividade.  
 Devem ser adicionados à base de cálculo, no mês em que forem auferidos, os ganhos de capital, as demais receitas e os resultados positivos decorrentes de receitas não compreendidas na atividade.

**Cálculo do Imposto - Lucro Estimado**

A alíquota para o IR é de **15%** e da CSLL é de **9%** sobre o Lucro Real apurado.   
 A parcela do Lucro Presumido que exceder ao resultado da multiplicação de **R$ 20.000,00** (vinte mil reais) pelo número dos meses do respectivo período de apuração, sujeita-se à incidência do adicional, à alíquota de **10%** (dez por cento).  
Podem ser deduzidos do imposto devido os seguintes valores:  
 a) Incentivos fiscais (Caráter Cultural e Artístico, Programa de Alimentação do Trabalhador, Desenvolvimento Tecnológico Industrial/Agropecuário - aprovados até 31/12/2005, Atividade Audiovisual, Fundos do Direito da Criança e do Adolescente, Regionais de Redução e/ou Isenção do Imposto, Isenção/Prouni, Redução por Reinvestimento, Atividades de Caráter Desportivo, Fundos Nacional, Estaduais ou Municipais do Idoso e Remuneração da Prorrogação da Licença-Maternidade;  
 b) o IR pago ou retido na fonte sobre as receitas que integram a base de cálculo do imposto devido;  
 c) Imposto pago no exterior sobre lucros disponibilizados, rendimentos e ganhos de capital;  
 d) o imposto retido na fonte sobre rendimentos pagos ou creditados a filial, sucursal, controlada ou coligada de pessoa jurídica domiciliada no Brasil, não compensado;  
 e) o IR retido na fonte por órgãos públicos, conforme art. 64 da Lei nº 9.430, de 1996;  
 f) o IR retido na fonte por Entidades da Administração Pública Federal (Lei nº 10.833/2003, art. 34).

São permitidas as seguintes compensações:  
 a) pagamentos indevidos ou a maior de imposto de renda;  
 b) saldo negativo de imposto de renda de períodos anteriores;  
 c) outras compensações efetuadas mediante Declaração de Compensação (PER/DComp) ou processo administrativo.  
 A apuração pelo Lucro Estimado á acumulativo, ou seja, serão consideradas na apuração todas as movimentações das Contas Contábeis desde o primeiro mês do ano até o mês da antecipação.   
 Os pagamentos mensais poderão ser suspensos ou reduzidos uma vez que os valores sejam demonstrados através da elaboração de balanço, ou balancetes de suspensão ou redução.  
 Para isso o valor do imposto devido no período em curso deve ser igual ou inferior à soma do imposto devido por estimativa até o anterior àquele a que se refere o balanço ou balancete levantado.

***Nota Importante*:** Para a correta apuração dos tributos neste regime e geração das informações para o arquivo texto da ECF os seguintes pontos devem ser observados:  
1 - Os períodos de apuração por estimativa (mensais) devem ser encerrados antes do período anual.  
2 - Os DARF´s para recolhimento devem estar gerados e integrados ao financeiro. Só serão selecionados para o cálculo do Tributo devido os DARF´s integrados e baixados.  
3 - Se não existir integração com o financeiro os valores pagos por estimativa não serão considerados na apuração do tributo do período anual. Neste caso os valores deverão ser informados manualmente no PVA no campo respectivo.  
4 - O período de apuração anual (real) deve ser encerrado para que os valores pagos por estimativa sejam considerados no valor do tributo a pagar. No anexo Detalhamento da Apuração será gerada uma linha com a origem **Apuração**seguindo a regra abaixo:

1
incomplete
Para o tributo IRPJ será gerada uma linha com o somatório de todos os valores do  tributo (IRPJ) pagos por estimativa  com o código 24 ([tabela dinâmica da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422546165)) quando a qualificação da pessoa jurídica for PJ em Geral. Esta qualificação é informada nos [parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) no cadastro da Filial. Para a classificação Demais empresas será gerada uma linha com o código 21 (tabela dinâmica da ECF). Esta informação será gerada no [Registro N360](http://tdn.totvs.com/pages/viewpage.action?pageId=422545978) do arquivo texto da ECF.

2
incomplete
Para o tributo CSLL será gerada uma linha com o somatório de todos os valores do tributo (CSLL) pagos por estimativa com o código 21 (tabela dinânimca da ECF). Esta informação será gerada no [Registro N670](http://tdn.totvs.com/pages/viewpage.action?pageId=422545978) do arquivo texto da ECF.
