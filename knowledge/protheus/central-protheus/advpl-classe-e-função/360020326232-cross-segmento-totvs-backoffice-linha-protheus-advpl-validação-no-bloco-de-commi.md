---
article_id: 360020326232
category: ADVPL - Classe e Função
content_hash: f14f80132eb34dc398930365addeffb10e023a51501ed5faf1d26f47bf1e13e9
fetched_at: '2026-06-28T22:40:18.200227+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Validação no bloco
  de commit
type: support-article
updated_at: '2022-06-01T12:11:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020326232-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Valida%C3%A7%C3%A3o-no-bloco-de-commit
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min   
  
Dúvida**Ao utilizar o quarto parâmetro do construtor da classe MPFormModel para sobrescrever o bloco de gravação (*commit*) percebemos que se retornado falso, é gerada uma mensagem de ajuda e ele não prossegue com a gravação, assim como, se retornado verdadeiro, é exibida uma mensagem de sucesso.

Isso não seria uma validação do bloco de persistência (*commit*)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.8  
  
**Solução**O retorno falso do bloco de gravação na verdade atende a uma necessidade específica do EAI (*Enterprise Application Integration*) e não deve ser utilizado.

Dentro do bloco de *commit* todas as validações do sistema já devem ter sido realizadas e não deve ser retornado falso neste bloco.

Caso aconteça algum erro durante a gravação, o sistema deve ser abortado por erro (pode ser utilizada a função Final()), pois dependendo do erro ocorrido dentro da gravação o sistema precisa ser finalizado para manter a integridade dos dados.  
 **Observação**Apesar da sobrescrição do bloco de persistência ser possível, orientamos que o mesmo não seja realizado, principalmente em fontes do padrão.

Para interceptar o *commit* e incluir novas gravações no mesmo é recomendado utilizar os eventos do MVC disponível por meio do método InstallEvent() da classe MPFormModel() e os momentos da classe FwModelEvent().  
 **Saiba mais**[Final - Finaliza o sistema](http://tdn.totvs.com/display/public/PROT/Final+-+Finaliza+o+sistema)[Interceptação do Commit e Validação MVC - FWModelEvent](http://tdn.totvs.com/pages/viewpage.action?pageId=269552294)
