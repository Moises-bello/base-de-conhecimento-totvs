---
content_hash: a8e456309986b6f3aaa968287544b18db4ecdd730a1e1ad2acd8eb6f71779f7d
fetched_at: '2026-06-29T00:10:10.705991+00:00'
page_id: '452719912'
product: rm
source: tdn-rm
title: 13º Salário - Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719912
version: 6
---

Nesta etapa será configurado como será lançado o 13º na rescisão.  
   
**Parâmetros**  
Lança eventos adicionais de 13º na rescisão  
Com este parâmetro marcado, ao calcular a rescisão do funcionário o sistema lançará na rescisão, os eventos informados em Configurações | Parâmetros | Parametrizador | Folha de Pagamento | 13º Salário | Eventos Adicionais Globais  
   
Separar médias de 13º salário na rescisão

Funcionários temporários recebem 13º salário

Com este parâmetro marcado, no cálculo da rescisão de funcionários temporários, será incluído o cálculo do 13º salário rescisão automaticamente.

Considera faltas para o cálculo de 13º salário na rescisão

Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão

Marcando esse parâmetro quando existir restituição será criado o período de retificação (10000) com os valores restituídos e dois eventos de base de cálculo da diferença encontrada entre o valor calculado para 13º na rescisão e o desconto de 13º adiantado como 2ª parcela de 13º salário. Um evento será a Base Cálculo para estornar INSS e deve ter a incidência estorna INSS 13 marcada e outro evento será a Base de Cálculo para estornar IRRF e deve ter a incidência estorna IRRF 13 marcada. 

Serão lançados também dois eventos de pagamento no período de cálculo da rescisão com os valores de restituição de INSS 13º e IRRF 13º como provento Estes eventos não devem ter incidência.

No período retificado será  lançando o evento com o código de cálculo 383 - Líquido retificação para zerar o período 10000 

Para identificar qual período é de pagamento de 13º Salário, será verificado a existência de evento de código de cálculo 102 - 2ª parcela de 13º salário.

Caso o parâmetro esteja desmarcado ou o cálculo não encontre período de pagamento de 13º Salário, ou seja, não encontre o evento com  código de cálculo 102 - 2ª parcela de 13º salário, então será lançado os valores de restituição como ocorre atualmente na rescisão e deverá retornar a mensagem: ‘O sistema identificou restituição de INSS para o funcionário de chapa XXXXX. Porém, para o eSocial não é permitido ter restituição de INSS em período onde não consta o desconto com valor igual ou superior ao valor da restituição.”

AtençãoNão haverá a retificação automática em casos de pagamento do 13º Salário (código de cálculo 102 - 2ª parcela de 13º salário) antes de Dezembro. Neste caso, como isto geralmente é customizado, o tratamento também deve ser customizado caso não queira lançar restituição na rescisão.  Em competências diferentes de dezembro seguirá o comportamento atual. EXEMPLO DE CÁLCULO

[FAQ - Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873208316)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Retornar para **Rescisão**
