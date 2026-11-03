---
article_id: 360039207953
category: Férias
content_hash: 68e652d4fa9dd789aef54f2eaa4ad8cfdc029ca1fb1bf67515c8eaa946b85bdc
fetched_at: '2026-06-28T22:46:56.418051+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias Coletivas: mudança do período aquisitivo para menores
  que 1 ano de admissão'
type: support-article
updated_at: '2025-01-22T18:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039207953-RH-RM-FOP-F%C3%A9rias-Coletivas-mudan%C3%A7a-do-per%C3%ADodo-aquisitivo-para-menores-que-1-ano-de-admiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29425588139287)Tempo aproximado para leitura: **00:01:15 min  
  
Dúvida**Como o sistema irá alterar o período aquisitivo quando houver Férias Coletivas para funcionários com menos de 1 ano de admissão ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Considerando os termos do **art**. **140** da CLT, em sendo prática da empresa conceder férias coletivas e não tendo o empregado ainda completado 12 meses de trabalho, terá ele direito a férias proporcionais, iniciando-se, na oportunidade, novo período aquisitivo.  
  
O produto libera para o Cliente parametrizar conforme necessidade da Empresa a data do novo período aquisitivo, pois a legislação poderá ser interpretada com ambiguidade. Portanto, segue opções disponibilizadas pelo produto:  
  
**Cenário de exemplo:**

* Período Aquisitivo do Funcionário:  02/08/2019 - 01/08/2020
* Férias Coletivas:  20/12/2019 até 31/12/2019

Ao acessar: **Folha de Pagamento | Configurações | Parametrizador | Férias | Férias Coletivas**, terá os seguintes parâmetros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29425588145815)  
  
**Considera data de retorno para inicio período aquisitivo quando <1 ano**

* **Parâmetro desmarcado:** No cenário de exemplo, se este parâmetro estiver desmarcado, ao finalizar as férias do funcionário, o produto irá considerar um dia anterior a data início de gozo, ou seja, a data fim do período aquisitivo será modificada para 19/12/2019.
* **Parâmetro marcado:** No cenário de exemplo, se este parâmetro estiver marcado, o sistema irá considerar a data fim das férias, ou seja, a data fim do período aquisitivo será modificada para 31/12/2019 na finalização das férias.

**Mantem período aquisitivo quando <1 ano**

* **Parâmetro marcado:** Se marcado, o sistema não altera a data do período aquisitivo.
* **Parâmetro desmarcado:** Se desmarcado, irá alterar o Período Aquisitivo dos menores que 1 ano, conforme a situação atual do parâmetro **Considera data de retorno para inicio período aquisitivo quando <1 ano.**

**Importante**A alteração do Período Aquisitivo é feita automaticamente quando as férias forem finalizadas. Além disso, é importante ressaltar que o cadastro das Férias Coletivas deverá ser feito através da rotina: **Férias | Coletivas Globais** e o parâmetro **Férias Coletivas** deve estar marcado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29425588154135)
