---
article_id: 28206773411095
category: Integrações - Feedz
content_hash: 748fb5785c5121155daa91c496c8442ab796503a9676c348fa75742baaeef754
fetched_at: '2026-06-28T22:46:41.474433+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: RH - RM - FOP - Integração RM Labore x Feedz - Nenhum funcionário atende a
  seleção
type: support-article
updated_at: '2024-12-02T17:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28206773411095-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-Feedz-Nenhum-funcion%C3%A1rio-atende-a-sele%C3%A7%C3%A3o
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28206807256087) Tempo aproximado para leitura: **00:02:50 min****Ocorrência**Ao realizar o envio de funcionário da aplicação RM para a plataforma da Feedz, é retornado o erro "Nenhum Funcionário atende a seleção".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
**Causa**O erro acontece pois a Função à qual o funcionário está alocado não possui o cargo registrado em seu cadastro, ou o funcionário está com históricos incompletos.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1.1 Acesse o Cadastro do Funcionário na aba **Registro** e clique no ícone de três pontos para editar a função;  
1.2. Edite a **Função** do funcionário;  
1.3. Informe o **Cargo** dentro do registro da Função que o funcionário exerce;  
1.4. Execute a integração **TOTVS RH Performance e Metas / Feedz** novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28206773384855)

2.1 Caso ainda seja apresentado o erro mesmo após o preenchimento do cargo, faça a verificação dos históricos do funcionário através do menu **Folha de Pagamento | Folha Mensal | Validações | Validação da Base de Dados.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28206807260695)

2.2 No fim da execução da rotina, obtenha o log **Funcionário** e faça os ajustes necessários que forem identificados referente aos **Históricos** para a chapa com problemas de integração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28206773388439)

Saiba mais  
[Integração RM X Feedz](https://tdn.totvs.com/pages/releaseview.action?pageId=785614408#1-2)
