---
article_id: 360019473052
category: ADVPL - Classe e Função
content_hash: 7190685b2b1ecc2c2d565c9c539798a85ea83313759babddaf2512f496a7c8fd
fetched_at: '2026-06-28T22:40:19.239110+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro: it wasn''t
  possible to obtain exclusive acess to the objects repository'
type: support-article
updated_at: '2022-01-10T14:00:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019473052-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-it-wasn-t-possible-to-obtain-exclusive-acess-to-the-objects-repository
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Ao tentar compilar um arquivo (imagem, fonte e etc.) no repositório de objetos (RPO) é exibido a seguinte mensagem de erro no console do IDE (*Integrated Development Environment*):

```
Erro de compilação: Cannot open RPO File. Check file access permissions / Read-Only status.   
It wasn't possible to obtain exclusive access to the objects repository 
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Este erro ocorre quando o IDE não conseguiu acessar o repositório de objetos para compilar o arquivo.

Dos motivos que podem gerar este erro são eles:

1. RPO encontra-se em uso por terceiros
2. Privilégios de acesso
3. Servidor deixou de responder
4. Ambiente inexistente

**Solução**As soluções serão apresentadas em tópicos numerados de 1 à 4 de acordo com as causas dos itens acima:

1. Verificar por meio do TOTVS Monitor se existem usuários logados e/ou validar se no momento existem *jobs* schedulados em processo (seção ONSTART) e derrubá-los/removê-los temporariamente:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015293572/mceclip0.png)  
     
   Outra solução seria adicionar na seção GENERAL, adicionar a chave BUILDKILLUSERS. Pois com o uso da mesma, ela irá forçar que todos os usuários e processos sejam conectados, dado prioridade para compilação:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015343531/mceclip1.png)
2. Dependendo do sistema operacional, verifique os acessos de modo à permitir que o IDE conseguir ler/escrever no arquivo:  
     
   **Windows**:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015294492/mceclip6.png)  
     
   **Linux**:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015344231/mceclip5.png)
3. Algumas vezes o servidor pode deixar de responder por algum motivo (alto índice de threads de consumo, processos de compilação concorrentes e afins), assim sendo, torna-se necessários reiniciar o AppServer e tentar novamente.
4. Por algum motivo do cliente, o ambiente pode ser renomeado, assim sendo, uma vez que o IDE esteja conectado em um ambiente que não mais exista, e tente-se efetuar a compilação, será gerado o erro citado no item 4.

**Saiba mais**  
[Chave BUILKILLUSERS](http://tdn.totvs.com/pages/viewpage.action?pageId=210044134)  
[Seção ONSTART](http://tdn.totvs.com/pages/viewpage.action?pageId=6064858)  
[Permissões linux](https://pt.wikipedia.org/wiki/Chmod)  
[Permissões windows](https://pt.wikihow.com/Modificar-as-Permiss%C3%B5es-de-Arquivos-no-Windows-7)
