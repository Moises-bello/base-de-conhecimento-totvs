---
content_hash: a32ee7d14450dcfc6e6eb0e6cf1c999559f851672eaf570481af97524fbe85d1
fetched_at: '2026-06-29T00:10:07.095309+00:00'
page_id: '452719364'
product: rm
source: tdn-rm
title: Contabilização - FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719364
version: 2
---

Nesta é etapa é configurada como será feita a contabilização da Folha de Pagamento.  
    
 **Parâmetros**  
 Usa histórico de rateio de encargos na contabilização retroativa  
 Com este parâmetro marcado, será guardado o histórico de rateio fixos de encargos gerados pela contabilização. Este histórico poderá ser verificado em Encargos | Contabilização | Históricos | Encargos | Anexos | Rateio de Encargos por Centro de Custo. Este parâmetro tem o objetivo de atender a necessidade de gerar a contabilização de encargos retroativa e que sejam respeitados os rateios da época. Para tanto, o cliente deve utilizar Cálculo por Centro de Custo.

**Observação**  
 Este parâmetro estará habilitado somente se o parâmetro "Utiliza Cálculo por Centro de Custo" da etapa 'Cálculo'.  
 Usa filial contábil na seção quando utiliza cálculo por centro de custo  
 Com este parâmetro marcado, no lote contábil, será considerada a filial contábil do cadastro de seções, da aba Dados Contábeis.

**Observação**  
 Este parâmetro estará habilitado somente se o parâmetro "Utiliza Cálculo por Centro de Custo" da etapa 'Cálculo'.  
 Inibe reversão de valores na provisão mensal de férias  
 Marcando este parâmetro, no momento da contabilização do encargo de férias, o sistema irá contabilizar como valor de encargo de férias o valor do avo adquirido no mês. Evitando desta forma, valores negativos no encargo de provisão de férias e a consequente reversão das contas. Assim, os valores de férias pagos aos funcionários poderão ser contabilizados através dos eventos de férias presentes na movimentação.

**Atenção**  
 Caso o usuário já tenha gerado o histórico de Provisões dentro da competência e alterado este parâmetro, o histórico de provisões deverá ser gerado novamente para refletir as alterações.   
    
 **Exemplo**  
 Parâmetro Marcado

|  |  |
| --- | --- |
| Provisão Acumulada de férias | Valor contabilizado baseada na provisão mensal |
| 1200 | 100 |
| 1300 | 100 |
| 1400 | 100 |
| **300** | **100** |

Funcionário tirou férias. Ao contabilizar a provisão mensal de férias, o sistema abate o valor das mesmas (Salário de 1500,00 menos férias no valor de 1200,00 = Provisão de férias = 300,00)  
 O sistema gera o lançamento de contábil no valor de 100,00. Para calcular esse valor, o sistema considera o valor da provisão acumulada sem abater o valor das férias pagas ao funcionário e contabiliza apenas o valor do avo de férias. Desta forma o valor não ficará negativo e consequentemente não ocorre a inversão das contas contábeis do encargo de férias.   
    
 Parâmetro Desmarcado

|  |  |
| --- | --- |
| Provisão Acumulada de férias | Valor contabilizado baseada na provisão mensal |
| 1200 | 100 |
| 1300 | 100 |
| 1400 | 100 |
| **300** | **-1100** |

Funcionário tirou férias. Ao contabilizar a provisão mensal de férias, o sistema abate o valor das mesmas (Salário de 1500,00 menos Férias no valor de 1200,00 = Provisão de Férias de 300,00).  
 O Sistema gera o lançamento contábil no valor de 1100,00. Sendo esse, o valor da provisão do mês atual menos o valor da provisão do mês anterior, que ficará negativo ocorrendo então a inversão das contas contábeis.  
 Com o parâmetro marcado o sistema guarda os seguintes valores no histórico de provisões:

* **Valor:** O valor da provisão de férias abatendo férias no mês ou não, conforme parametrizado pelo usuário no campo "Abate o valor das férias do mês" no momento da geração do histórico de provisões.
* **Valor (com abatimento no mês):** O valor da provisão com abatimento das férias do mês.
* **Valor (sem abatimento no mês):** O valor da provisão sem abatimento das férias do mês.
* **Valor pago de férias no mês:** Este campo será preenchido com o valor da provisão com abatimento das férias do mês, menos o valor da provisão sem abatimento das férias do mês. Veja o exemplo abaixo:

Valor pago de férias no mês: R$ 4257,07 (Valor provisão (sem abatimento no mês) menos o valor da Provisão com abatimento no mês)  
 Provisão sem abatimento no Mês:R$4966,58  
 Provisão com abatimento no mês:R$709,51

Permite contas iguais e debito e a crédito  
 Quando marcado este parâmetro, é possível processar a contabilização com a mesma conta de débito e crédito para um evento ou encargo. Entretanto, para compatibilizar com o TOTVS Gestão Contábil, serão gerados dois lançamentos, sendo um lançamento para débito e outro para crédito.   
 Se desmarcado, o TOTVS Folha de Pagamento impede que a mesma conta seja utilizada simultaneamente  para débito e crédito.  
    
 Provisão de férias/13º obrigatório  
 Empresas que utilizam contabilização de encargos de provisão de férias e 13° salário devem, preferencialmente, marcar este parâmetro. Se este parâmetro for desmarcado, ele permite que geração do histórico de provisões na liberação de competência e na contabilização deixe de ser obrigatória. O sistema só permite gerar dados contábeis de encargos se obrigatoriamente o histórico de provisões foi gerado. É importante lembrar que na contabilização dos encargos acima, o sistema usa o histórico de provisões do mês atual e mês anterior, portanto, a partir do momento que este parâmetro é ativado, os resultados esperados só devem acontecer no mês competência posterior. Também, se a empresa não utiliza a contabilização destes encargos, o usuário poderá desativar este parâmetro, para evitar mensagens de alertas cada vez que é acionada a liberação de competência ou contabilização. Quando o parâmetro estiver desmarcado, a geração de histórico permanece ativa, pois o usuário pode gerenciar a tarefa.

**Observação**  
 Com este parâmetro marcado só é permitido fazer a liberação de competência após a geração do histórico de provisão.   
 Usa Departamento  
 Parâmetro disponível somente para visualização, que é exibido quando tem integração com TOTVS Gestão Contábil. Ele é configurado no TOTVS Gestão Contábil.  
    
 Segue regras do RM Saldus na geração de Lançamentos   
 Com este parâmetro marcado, o sistema utilizará as regras do módulo TOTVS Gestão Contábil na geração de lançamentos. Entre elas:

* Irá realizar a distribuição Gerencial conforme parametrizada na conta contábil do Plano de Contas Contábil.
* Irá realizar a consistência de lançamentos conforme a opção "Amarração de lançamentos" do TOTVS Gestão Contábil.

Gera contabilização no Labore antes de enviar para o Saldus  
     
 Gerar rateio contábil com base na movimentação de ensino e movimento temporário   
 Marcando este parâmetro, o rateio dos eventos por centro de custo, item contábil e classe de valor será calculado verificando os parâmetros "Segue rateio movimento temporário" e "Segue rateio movimento ensino" presente no cadastro de eventos.

* Se no cadastro do evento estiver marcado o parâmetro "Segue rateio movimento temporário" o rateio do evento será calculado buscando as informações na tabela PFMOVTEMP para a mesma competência dos lançamentos contábeis.
* Se no cadastro do evento estiver marcado o parâmetro "Segue rateio movimento de ensino" o rateio do evento será calculado buscando as informações na tabela PFMOVENSINO para a mesma competência dos lançamentos contábeis.

**Observação**  
 Este parâmetro ficará visível somente se a integração com outros BackOffices estiver ativa e se o Labore estiver integrado com o Educacional e/ou Chronus.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Voltar para tela anterior **Folha Normal**
