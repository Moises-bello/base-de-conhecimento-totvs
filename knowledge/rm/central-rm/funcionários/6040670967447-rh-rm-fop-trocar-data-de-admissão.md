---
article_id: 6040670967447
category: Funcionários
content_hash: cbadf0b00392aeb28e8cce2ccc6c16ffc4147ea6f7e69d3a9efad5ef8d80c2eb
fetched_at: '2026-06-28T22:47:03.316551+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Trocar Data de Admissão
type: support-article
updated_at: '2025-03-11T10:06:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6040670967447-RH-RM-FOP-Trocar-Data-de-Admiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24286595853079) Tempo aproximado para leitura: **00:02:15 min****Dúvida**Como realizar a troca de data de admissão do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches 12.1.33.197 ou superiores.  
  
**Solução**Este processo tem a função de realizar a alteração da data de admissão do funcionário e seus devidos históricos e período aquisitivo.   
  
**Importante**

* Alterações poderá ser realizado somente em funcionários admitidos no mês ou próximo mês.
* Será gerado gatilho de gatilho de inclusão ou retificação dos eventos S-2200 ou S-2300.
* Caso tenha alguma produção lançada anterior a nova data de admissão não será realizado a alteração para funcionários **tipo Rural**.

Para realizar a alteração de data de admissão, siga os passos abaixo.   
  
1. Acesse o menu **Serviços Globais | Segurança | Perfis**, selecione o sistema **Folha de Pagamento**, edite o perfil desejado, vá em acesso aos menus e permita o acesso **01.01.01.257 Histórico Afastamento: Trocar Data de Admissão**:  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10317193969687)**2. Acesse o menu **RH | Folha de Pagamento | Administração de Pessoal | Funcionários**, selecione o funcionário desejado e acesse **Processos | Trocar Data de Admissão**:![](https://centraldeatendimento.totvs.com/hc/article_attachments/30557034571543)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10317303160727)  
  
3. Informe a **Quebra de Seção** | em **Seleção de funcionários** informe a chapa do funcionário e preencha a data da **Admissão atua**l, a **Nova admissão** e execute o processo:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10319874512151)  
  
4. Processo executado com sucesso:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10319813451287)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10319859432727)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10319969960087)  
  
**Saiba mais**[Trocar Data de Admissão](https://tdn.totvs.com/pages/releaseview.action?pageId=655883002)
