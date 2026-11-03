---
content_hash: f62af36f63a7be5e140e28f89fe1ad95b4efab515d0c1a35c0d0637f70b6c4cf
fetched_at: '2026-06-29T00:10:03.876731+00:00'
page_id: '452719168'
product: rm
source: tdn-rm
title: Cálculo 1/2 - Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719168
version: 8
---

O objetivo desta etapa é definir como será configuração de alguns parâmetros de Cálculo de Férias.  
**Parâmetros**  
Paga Adiantamento nas Férias  
Com este parâmetro marcado, os sistema irá calcular junto com as férias o adiantamento de salário (correspondente aos dias trabalhados no mês de início de gozo).

**Atenção**  
Para que seja efetuado o cálculo do adiantamento no recibo de férias, é necessário que no cadastro do funcionário que seja informado o percentual de adiantamento no campo '% Adiantamento' em Administração de Pessoal | Cadastros | Funcionários, menu Informações para o Cálculo | Parâmetros.  
O evento com o código de cálculo 34 deve está cadastrado na base.   
   
Paga adicional constitucional sobre dias de direito de férias  
Com este parâmetro marcado, o sistema calculará o adicional constitucional sobre o saldo de férias. Com este parâmetro desmarcado, o sistema calculará o adicional para férias sobre os dias de gozo de férias, desconsiderando faltas, abono pecuniário, etc.    
   
Ignora eventos que incidem em salário  
Com este parâmetro marcado, o sistema irá desconsiderar os eventos que incidem em salário para os cálculos da base de Férias.  
   
Considera eventos que incidem em salário somente no Recibo  
   
   
Usa regime de tempo parcial  
Com este parâmetro marcado é habilitado o campo Dias Direito (Jorn. Reduzida), no cadastro de Funcionários no menu Informações para o Cálculo | Parâmetros. Se o usuário informar um valor para este campo, o sistema irá considerar como dias de direito o mesmo valor informado.

**Exemplo**  
Informo no campo Dias Direito (Jorn. Reduzida) = 20  
Funcionário com período aquisitivo já vencido, sem faltas.  
Quando o for marcar as férias ou no cálculo da rescisão, irá considerar 20 como direito para o cálculo das férias.   
   
**Observação**  
Caso informe 0 (zero) para o campo Dias Direito (Jorn. Reduzida), o sistema irá considerar como dias de direito o padrão do sistema.

Evento código de cálculo 107 inibe evento código de cálculo 30  
Se o parâmetro for marcado, ao ser lançado o evento com o Código de Cálculo 107 - IRRF FÉRIAS CALCULADO PELO USUÁRIO na movimentação do funcionário, o sistema irá zerar o evento com o Código de Cálculo 30 - IRRF FÉRIAS.   
Se o parâmetro não for marcado e, for lançado na movimentação do funcionário o evento com o CC 107 e este com valor menor que o evento de CC 30, que é calculado automaticamente pelo sistema, o sistema irá considerar os dois eventos. Esta diferença será lançada no evento de CC30. Caso valor do evento com o CC 107 seja maior ou igual ao valor do evento CC 30, o sistema irá zerar o evento com CC 30.

Lança eventos adicionais de férias em recibos com apenas abono

---

<< Retornar para **Férias**
