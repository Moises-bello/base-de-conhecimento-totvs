---
article_id: 4404665971095
category: Entrada de dados
content_hash: a7f503f0031cac6b15c87f8727275d170690cf96e2e14bd7b6ea4c7221db826e
fetched_at: '2026-06-28T22:46:30.577602+00:00'
product: rm
section_id: 1500000835061
source: central-rm
title: RH - RM - PTO - Importação de dados
type: support-article
updated_at: '2026-03-19T17:08:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404665971095-RH-RM-PTO-Importa%C3%A7%C3%A3o-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408785662231) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Como efetuar a importação de dados do ponto?  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**

Os dados que podem ser importados para o Automação de Ponto são:

**-** Parâmetros do Sindicato.  
**-** Cadastros de abonos  
**-** Dados específicos de funcionários Movimentos, Abonos, Abonos Futuros, Banco de horas por dia, Sobreavisos,  -Descanso e Extras Autorizadas:  
  
Para realizar a importação, acesse:

**1.** Módulo RH | Automação de Ponto  
**2.** Entrada de Dados | Importação de dados    
**3.** Clique em Avançar   
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13612787126039)**  
  
**Observação:** Será exibida a mensagem de aviso abaixo:   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404665714711)

**4.** Selecione os dados que se deseja importar e infome o caminho do arquivo txt contendo os dados.    
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404660394391)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404665750807)  
  
**Delimitador de Campos:** ; (ponto e vírgula)  
**Formato de data:** DD/MM/YYYY  
**Separador decimal:** , (vírgula)  
**Formato decimal:** 9999999999,99  
**Hora:** HHH:MM

**Importante**

1. Se algum campo não for informado, o sistema irá tentar realizar a inserção do campo nulo.
2. Os campos devem ser informados conforme a ordem descrita no layout.

**Saiba mais**

Para maiores informações sobre importação de dados, acesse [Importação de dados](https://tdn.totvs.com/pages/viewpage.action?pageId=452719584)  
Sobre outros layouts de importação, acesse:

**Layouts de importação**

* **Parâmetros do Sindicato**  
  [Layout - Parâmetros do Sindicato](https://tdn.totvs.com/pages/viewpage.action?pageId=572953789)
* **Outros Parâmetros**  
  [Layout - Outros Parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=572953813)
* **Dados dos Funcionários**  
  [Layout - Dados dos Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=572953897)
