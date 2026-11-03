---
content_hash: 898f384b30beedd702911e98303efbf374015ebf29223170bd24fed43f84e789
fetched_at: '2026-06-29T00:09:22.029583+00:00'
page_id: '422545951'
product: rm
source: tdn-rm
title: Apuração ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545951
version: 24
---

Por esta opção, o sistema irá gerar as guias de apuração de ICMS, respeitando as regras de ICMS vinculada aos lançamentos Fiscais.  
A apuração do ICMS é  fruto da diferença entre o imposto devido nas operações realizadas pelo contribuinte (Débito Fiscal) e o imposto suportado nas operações anteriores (Crédito Fiscal), em nome do Princípio da Não-cumulatividade constitucionalmente previsto.  
A apuração é realizada com base na escrituração de documentos fiscais movimentados durante o período (mês).   
Nos lançamentos fiscais de entrada/saída informamos o valor de ICMS que incidiram sobre a operação.   
A apuração é realizada, individualmente, por filial, através do encerramento do período criado mensalmente.

A data de vencimento deve ser informada pelo usuário, uma vez, que essa data é definida em função de cada Estado.

No encerramento do período o sistema totaliza os valores destacados nos lançamentos fiscais e apura o débito ou o crédito, através do regime débito/crédito. Se o saldo for credor este valor é transportado para o mês seguinte.

***Observação:***Só poderão ser incluídos lançamentos Fiscais e lançamentos de ajuste da apuração do ICMS se o período para o ICMS estiver cadastrado e com o STATUS="Aberto". Se um determinado período estiver encerrado, nenhuma operação que afeta a apuração é permitida pelo sistema.

falseApuracaoICMStrue1Apuração

Receita Bruta (VLRRECEITABRUTATOTAL): Deve receber a diferença positiva entre o Valor do Faturamento e o Valor Exclusões do Faturamento.  
Saldo Credor/devedor (SALDOTRBATUAL): Deve receber o valor do Saldo devedor apurado onde será aplicado a formula:(Receita Bruta \* Alíquota Apuração%) + (Saldo Lançamentos Outros Débitos e Créditos) + (Difal Entrada (Uso e Consumo ou Ativo Imobilizado)) + (Difal na Saída Devido ao Remetente).

***Observação***: Serão observados os parâmetros do Diferencial de Alíquota para o mesmo ser considerado no Saldo Credor\Devedor.

***Observação***: Não serão considerados para os cálculos da Apuração, os Lançamentos de Outros Débitos/Créditos contendo Sub Apurações de Ressarcimento

**Observação:** Serão considerados os [Códigos de Ajuste](https://tdn.totvs.com/x/-U90GQ) associados aos lançamentos de Entrada, Saída, Outros Débitos/Créditos para o cálculo da Apuração do ICMS e para a geração do registro E110, no arquivo do SPED Fiscal.

No Campo **Saldo Credor\Devedor** é considerado o **Valor de Ajuste do ICMS**, informado na Pasta de Ajuste do Lançamento Fiscal ou Item do Lançamento.

**Ajuste de Débito** (Considerado como Outros Débito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘3’, ‘4’ ou ‘5’ e o Quarto caractere for igual a “0”, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF30xxxxxx, UF04xxxxxx

**Ajuste de Crédito** (Considerado como Outros Crédito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘0’, ‘1’ ou ‘2’ e o Quarto caractere for igual a ‘0’, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF00xxxxxx, UF03xxxxxx.

3Outros Dados4Valores Adicionais Apuração

**Valores Adicionais Apuração**

Neste cadastro, é informado os valores declaratórios relativos ao ICMS, conforme definição da legislação estadual pertinente. Esses valores são meramente declaratórios e não são computados na apuração do ICMS, servem de base para a geração do Registro E115 do [SPED Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=422546128).

**Na apuração do Regime especial para empresa do RJ o valor da gorjeta não deve ser considerado na base do ICMS****(Alteração efetuada conforme RESOLUÇÃO SEFAZ N.º 322 DE 13 DE AGOSTO DE 2010)**

* Valor do Faturamento (VLRFATURAMENTO): Deve receber a soma do valor contábil de todos os lançamentos de saídas com Status "Normal" cujo CFOP associado seja do grupo 5.102 e cujo "Tipo de Devolução" (pasta Outros Dados no CFOP) seja Normal. Deste valor subtrai as operações de Entrada do tipo Devoluções que estejam vinculadas a saídas com CFOP 5.102.
* Valor Exclusões Faturamento (VLREXCRECEITAFINANCEIRA): Deve receber a soma do valor contábil de todos os lançamentos de saídas com Status "Normal" cujo CFOP associado seja do grupo 5.102, o "Tipo de Devolução" (pasta Outros Dados no CFOP seja Normal E o Tipo Tributação da Regra de ICMS seja "Isento" ou "Não Incidência" ou "Sem ICMS" ou "Suspenso".

***Observação***: Caso o tributo IPI esteja somando no Valor Contábil dos lançamentos fiscais selecionados o mesmo será subtraído.

5Valores Diferencial de Alíquota

No encerramento do período serão calculados os valores de Diferencial de Alíquota conforme parametrização prévia. Será realizado a validação de UF do emitente/destinatário sendo considerado o valor informado nos campos UF da tela de Coleta/Entrega, UF do Cli/For selecionado no campo "Cli./Forn. Origem / Destino" e campo UF do Cli/for do campo de Cliente/Fornecedor do lançamento fiscal respectivamente. Caso na validação seja encontrado uma operação interna com CFOP de DIFAL será apresentado a seguinte mensagem de inconsistência:  
  
"Erro no encerramento do(s) período(s):  
Período Filial X - Tributo ICMS - dd/mm/aaaa - dd/mm/aaaa:   
Erro na Apuração dos Valores de Diferencial de Alíquota. Erro:   
Há lançamentos com o estado do destino igual ao estado do remetente usando uma natureza interestadual, isso impede o cálculo do DIFAL.  
Verifique o correto preenchimento do campo Estado no Endereço de Coleta/Entrega, Cli/For de Origem Destino ou Cli/For respectivamente.  
Id. dos Lançamentos inconsistentes:  
YYYY"

falseAnexos2true1Guias GNR2Guias Normal3Subapuração
