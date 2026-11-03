---
article_id: 14562523013399
category: Encargos
content_hash: 4130e2f8242962153339fe7032c6658cbc24c0d06c8d1ec9c947d4f65951f682
fetched_at: '2026-06-28T22:46:52.311374+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do encargo  TIPO A  Valor calculado através de fórmula
type: support-article
updated_at: '2024-10-09T19:58:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14562523013399-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-A-Valor-calculado-atrav%C3%A9s-de-f%C3%B3rmula
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15588489954071) Tempo aproximado para leitura: **00:02:27 min****Dúvida**No módulo Folha de Pagamento como é a geração do encargo **TIPO A**  Valor calculado através de fórmula?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**A geração desse encargo é realizado através de fórmula, que sobrepõe os demais parâmetros do cadastro do encargo: Para criar este encargo acesse: **Encargos | Cadastros | Encargos**, e realize o cadastro conforme a necessidade da empresa.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15587972266007)  
  
O campo **Ordem de Cálculo** servirá para definir a prioridade e/ou ordem de cálculo  de um encargo do **tipo A - Valor calculado através de fórmula**, que utilizar o valor de um outro encargo do **tipo A - Valor calculado através de fórmula**, para retornar o valor através de uma variável de fórmula (VALENCARGOM) para o encargo que for receber o valor calculado no primeiro encargo.

**Exemplo:**

Encargo 0010 - Encargo 0010

Fórmula de valor:  RC \* 0,08

Ordem de cálculo: 1

Encargo 0009 - Encargo 0009

Fórmula de valor: VALENCARGOM('0010') + 100

Ordem de cálculo: 2  
  
**Importante**Neste caso a **Ordem de Cálculo** do encargo **Encargo 0010** deverá ser menor que a **Ordem de cálculo** do encargo **Encargo 0009** e a **Fórmula de valor** do encargo **Encargo 0009** deverá conter a variável VALENCARGOM para recuperar o valor.  
  
O campo **Ordem do cálculo** somente estará disponível para encargos do **tipo A - Valor calculado através de fórmula.**  
Exemplo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15588109304855)**Geração do encargo acesse: **Encargos | Geração dos encargos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15588015607447)  
  
Log da geração:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14562397278999)

**Importante**   
Verificar o código ativo associado ao cadastro do encargo pois no momento da geração do encargo será necessário selecionar o mesmo código ativo. Caso precise de apoio para criar o código ativo para vincular no encargo, utilize a documentação abaixo.   
  
[RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)  
  
**Saiba mais**

[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
