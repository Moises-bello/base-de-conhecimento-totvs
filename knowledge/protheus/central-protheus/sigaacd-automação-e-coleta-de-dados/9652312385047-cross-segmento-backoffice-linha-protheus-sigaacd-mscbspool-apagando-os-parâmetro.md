---
article_id: 9652312385047
category: SIGAACD - Automação e Coleta de Dados
content_hash: eed98c77609700cde9ceebab92967a83035f1338cd6dc4f329f011552cd46258
fetched_at: '2026-06-28T22:39:12.842761+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - MSCBSPOOL apagando
  os parâmetros. Como corrigir?
type: support-article
updated_at: '2024-10-07T19:46:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9652312385047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-MSCBSPOOL-apagando-os-par%C3%A2metros-Como-corrigir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26902242064407) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Ao reiniciar a rotina MSCBSPOOL, o mesmo  sempre vem desativado e perde os parâmetros já configurados. Como corrigir essa situação?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Para resolver esse problema execute os passos abaixo:

* Encerrar o MSCBPOOL (caso esteja aberto).
* Criar uma Pasta com o nome MSCBSPOOL no disco C:/ da sua máquina.
* Colocar o arquivo MSCBSPOOL.INI (Em anexo ao final desse artigo) na pasta criada no passo acima.
* Clicar com o botão direto em cima do arquivo e selecione a opção "Propriedades"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9651549662487)

* Na aba segurança certifique se as opções gravar, leitura e ler & executa estão marcados como permitir.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9651751470487)

* Após o procedimento feito acima é recomendado tanto o AppServer e o SmartClient serem  executados como Administrador.

Feito essas configurações acima não será mais perdido a configuração dos parâmetros da rotina MSCBSPOOL.

Caso o ambiente for Linux, complementar além dos procedimentos listados acima, com as orientações a seguir.

* No ambiente Linux o arquivo do MSCBSPOOL será criado dessa forma "/mscbspool/mscbspool.ini" .
* A rotina MSCBSPOOL para não apagar a configuração dos parâmetros no Linux, deve estar com a data do fonte 12/08/2024 ou superior. Caso não esteja com essa data ou superior a ela, é necessário verificar se está com a [última Expedição Contínua do Estoque Custos e Automação e Coleta de Dados em: Pacotes de Atualização - Estoque e Custos e Automação e Coleta de Dados](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602)
* Feito esses processos, executar  o AppServer e o SmartClient como 'Administrador'.

Realizando os procedimentos acima,  não será mais perdida a configuração dos parâmetros da rotina MSCBSPOOL.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*

*[MSCBSPOOL Configuração e local do arquivo de configuração.](https://tdn.totvs.com/pages/releaseview.action?pageId=525017741)*

*[MSCBSPOOL: Monitor de fila de impressão de etiquetas](https://tdn.totvs.com/pages/releaseview.action?pageId=570051440)*
