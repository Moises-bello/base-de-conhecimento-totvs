---
content_hash: 8789377448a4d1c170d031eb8af70122c4cc1a69bd7727527e317b059ee7b179
fetched_at: '2026-06-29T00:09:21.826234+00:00'
page_id: '422545924'
product: rm
source: tdn-rm
title: Bloco J - Plano de Contas e Mapeamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Bloco+J+-+Plano+de+Contas+e+Mapeamento
version: 10
---

Nesta etapa serão descritas as particularidades de cada registro do bloco J apresentado na ECF, extraídas do Totvs Gestão Contábil.

BLOCOJleftJ050J050

**Plano de Contas do Contribuinte**

Todas as contas do cadastro de plano de Contas Contábeis, da coligada ou Global, cujo campo "Natureza para emissão do SPED" estiver preenchido, serão apresentadas nesse registro com exceção da natureza "não informada". Para geração desse registro, o sistema também irá verificar o histórico de alteração da conta, caso o parâmetro "Enviar Histórico de alteração da Conta Contábil" esteja marcado.

J051J051

**Plano de Contas Referencial**

Nesse registro será gerado o mapeamento do plano de contas paralelo, conforme parametrização.

J053J053

**Sub Contas Correlatadas (Registro I053 ECD)**

Neste registro serão geradas as subcontas cadastradas no anexo da conta contábil (Anexo| Sub Contas Correlatadas).

Na adoção inicial da NOVA LEI 12.973 (Nova Lei Tributária), a empresa deverá evidenciar em ATIVO ou PASSIVO a diferença entre Ativos e Passivos pela Contabilidade Moderna (Lei nº6.404/76 c/ alterações) e a Contabilidade pelos critérios vigentes em DEZ/07 (Fiscal - RTT).   
Para poder excluir o saldo negativo ou não adicionar toda a diferença em JAN/15 no E-lalur da ECF (caso seja esta a opção) se o saldo for positivo,  a empresa deverá destacar a diferença em subcontas específicas.   
Portanto, se as empresas desejam controlar as diferenças existentes entre o saldo contábil (societário) e saldo fiscal (FCONT) existentes na adoção da lei 12.973, deverão criar subcontas em seu plano de contas para controle das adições e exclusões no LALUR – Livro de Apuração do Lucro Real (que se encontra dentro da ECF).  
Com o controle em subcontas não é necessário que as empresas realize o controle dos valores apurados, na parte B do LALUR. Exemplo numérico:  
Um veículo comprado em JAN/11, por R$ 700 e prazo de vida útil de 7 anos (sem valor residual) será depreciado por R$ 100 a cada ano na escrituração contábil, mas dedutível pelo FISCO em 5 anos (140). Em 31/DEZ/14, os saldos líquidos do Veículo serão:  
Saldo Contabilidade Moderna  -  R$ 300 Saldo Contabilidade DEZ/07  -  R$ 140 (RTT)

Diferença de Ativo Positiva de - R$ 160

Esta diferença (160) deverá ser transferida em JAN/15 para uma subconta, no mesmo grupo da conta original (veículo, cujo saldo será 140). Exemplo:

Veículo                       Dep. Acumulada Veículos    Veículo - Subconta (Lei 12.973 - Adoção Inicial)

700,00  |  1-160,00                            |    400,00         1-160,00             |

\_\_\_\_\_\_\_\_\_\_\_\_\_\_      \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_     \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

540,00  |                                             |  400,00                                     |

No exemplo acima, após a criação da subconta  podemos evidenciar que o saldo da conta Veículos será de 140 conforme citado no exemplo, chegamos neste valor subtraindo o saldo do Veículo R$ 540,00 menos a depreciação acumulada de R$ 400,00.  
O saldo total do grupo de veículos não será afetado, uma vez que temos na subconta o valor de R$ 160,00, que somado ao valor de R$ 540,00 chegamos em R$ 700,00.  
O valor registrado na subconta será utilizado para controle da adição/exclusão na ECF (dentro do LALUR). Portanto, o controle em subcontas nada mais é que o controle das diferenças entre saldo contábil e saldo fiscal como lançamentos contábeis para que a RECEITA FEDERAL possa conferir os valores que foram apurados pelas empresas.  
As empresas deverão realizar todo o levantamento das suas operações para que possam identificar quais serão as subcontas que devem ser criadas para este controle se desejado.

J100J100

**Centro de Custos**

O Totvs Gestão Contábil, permite que o plano de contas gerencial seja apresentado na Escrituração como informações de centro de custo. Para isso, acessar os parâmetros do Totvs Gestão Contábil | Rotinas Legais/Sped Contábil e marcar a opção "Conta Gerencial" no campo "Considerar para o Centro de Custo" A geração desse registro também respeitará as regras do parâmetro "Enviar Histórico de alteração do Centro de Custo".

**Lançamentos sem centro de custo**  
   
O PVA da ECF entende que se uma Conta Contábil teve movimentação com Centro de Custo, esta mesma Conta Contábil não pode ter movimentações sem Centro de Custo.  
Mensagem apresentada no PVA: *"Conta não é analítica. Esta conta e centro de custo devem estar cadastradas no plano de contas (J050/J051) e ser analítica."*  
   
Para estas situações, os usuários deverão ajustar as movimentações preenchendo o C. Custo ou então marcar no cadastro do Centro de Custo que o mesmo não será enviado para o SPED Contábil.  
Quando qualquer uma das situações acima ocorrer é importante que o processo de Associação Dinâmica de C. Custo seja executado para que os mapeamentos referenciais sejam atualizados.  
Com objetivo de auxiliar nesta solução, foi disponibilizado nos parâmetros do sistema uma opção que identifica o Centro de Custo que o sistema preencherá nas movimentações das Contas Contábeis que estiver no cenário relatado acima. Parâmetros >> Rotinas Legais >> SPED Contábil  
   
  
   
Exemplo:

| Conta Contábil | C. Custo | Valor |
| --- | --- | --- |
| 1.1.1.0001 | 01.01 | 1000,00 |
| 1.1.1.0001 | 01.02 | 3000,00 |
| 1.1.1.0001 |  | 4000,00 |

Centro de Custo criado e informado no parâmetro: 999- Sem Centro de Custo. Após executado o processo de associação dinâmica de centro de custo:

| Conta Contábil | C. Custo | Valor |
| --- | --- | --- |
| 1.1.1.0001 | 01.01 | 1000,00 |
| 1.1.1.0001 | 01.02 | 3000,00 |
| 1.1.1.0001 | 999 | 4000,00 |

O sistema preencherá esta informação somente na geração do arquivo, este procedimento não será realizado nas movimentações contábeis já cadastradas na base de dados.  
O preenchimento será realizado somente se houver para a Conta Contábil movimentação com C. Custo preenchido e movimentação para a mesma  Conta Contábil sem C. Custo preenchido.
