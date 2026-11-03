---
article_id: 38279090254103
category: Meu RH - Requisições
content_hash: 874344bd6672eecffdd47e4ed127c0213a75e67dccc3ac4df907c7dfd9d12cbd
fetched_at: '2026-06-28T22:47:28.022844+00:00'
product: rm
section_id: 26902073559319
source: central-rm
title: 'RH - RM - Meu RH - Erro ao aprovar requisição: A data prevista informada é
  menor que a data atual'
type: support-article
updated_at: '2026-03-05T20:57:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38279090254103-RH-RM-Meu-RH-Erro-ao-aprovar-requisi%C3%A7%C3%A3o-A-data-prevista-informada-%C3%A9-menor-que-a-data-atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38279084735383) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Ao tentar realizar a aprovação de uma requisição no portal Meu RH, é apresentada a mensagem de erro: **“A data prevista informada é menor que a data atual. Para prosseguir, é necessário editar a requisição e ajustar a data prevista.”**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2510.156  
  
**Solução**  
Nas requisições, existe a Validação da Data Prevista da Requisição

Ao realizar a **aprovação individual** de uma requisição, o sistema valida a **Data Prevista** informada.

* Caso a **Data Prevista** esteja **inferior à data atual** (por exemplo, data prevista em 12/01 quando a data atual é 13/01), a aprovação será bloqueada, retornando a mensagem em questão.

**Para resolver a situação**, dentro da visão de Requisições, o gestor deve editar a requisição antes de fazer a aprovação da mesma.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38836983676567)

Edite o campo Previsão, informando uma nova data de previsão para a requisição, lembrando que esta data deve ser igual ou superior a data atual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38836967474071)

Informada uma nova data, na parte inferior da tela será habilitado o botão de próxima etapa, sendo possível prosseguir com a aprovação da requisição á partir desta tela.

**ATENÇÃO!**

Caso deseje desativar essa validação, á partir das versões 12.1.2510.182 e 12.1.2602.105 é possível realizar essa ação.

Para isso, o parâmetro **"Ignorar validação de Data Prevista no avanço de etapa de requisições através da Grid"** deve estar marcado. Quando habilitado, o sistema permitirá o avanço de etapa através da grid de requisições mesmo que a Data Prevista seja inferior à data atual.

Caminho do parâmetro: Módulo Gestão de Pessoas > Configurações > Parametrizador > Portal Meu RH > Configurações > "Ignorar validação de Data Prevista no avanço de etapa de requisições através da Grid".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38836983682455)

Observação: Essa validação **não é aplicada na aprovação em lote**, devido a impactos de **performance**.

**Saiba mais:**

[19.1 Desligamento](https://tdn.totvs.com/display/NPR/19.1+Desligamento)  
[19.2 Substituição](https://tdn.totvs.com/pages/viewpage.action?pageId=581868464)  
[19.3 Alteração de salário, cargo e função](https://tdn.totvs.com/pages/viewpage.action?pageId=648020823)  
[19.4 Aumento de Quadro](https://tdn.totvs.com/display/NPR/19.4+Aumento+de+Quadro)  
[19.5 Transferência](https://tdn.totvs.com/pages/viewpage.action?pageId=684012675)
