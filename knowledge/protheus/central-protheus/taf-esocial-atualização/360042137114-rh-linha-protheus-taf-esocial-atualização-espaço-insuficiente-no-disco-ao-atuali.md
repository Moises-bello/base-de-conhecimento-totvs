---
article_id: 360042137114
category: TAF - eSocial - Atualização
content_hash: cf3400354192a7913ec74c15ffc80f6d380c272696e6174303f0f1ec11c2ff1e
fetched_at: '2026-06-28T22:45:13.319929+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Atualização - Espaço insuficiente no
  disco ao atualizar o TAF
type: support-article
updated_at: '2024-09-25T11:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042137114-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Espa%C3%A7o-insuficiente-no-disco-ao-atualizar-o-TAF
---

**Ocorrência:**

Ao utilizar o atualizador para o TAF o TSS ocorre o erro abaixo. (Espaço insuficiente no disco):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056138194)

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Causa**

Esse erro é causado pela falta de espaço no disco onde o TAF e o TSS estão instalados. Durante o processo de atualização do ambiente, o atualizador cria arquivos de backup, o que consome espaço em disco.

**Solução**

1 - Libere espaço suficiente no disco onde o TAF e o TSS estão instalados e, em seguida, execute o atualizador novamente.

**Importante!**

Se você executou o atualizador mais de uma vez, novas pastas de backup serão geradas, como exemplificado na imagem abaixo. Mantenha o primeiro backup em seu diretório e mova as outras pastas para outro disco. No entanto, nunca exclua o primeiro registro de backup antes de atualizar com sucesso o ambiente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056140814)

**PONTO DE ATENÇÃO:**

  

Caso o TAF esteja instalado em um disco local diferente do padrão "C:":

Exemplo: Instalado na unidade D:  
Os backups serão salvos na pasta TEMP no disco local C:.

**Exemplo:**

Esteja instalado na unidade D:\  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057264813)  
O backup será salvo na pasta **TEMP** no disco local **C:\**.

  

**Sugestão:**

Se não for possível liberar espaço na unidade C:, será necessário alterar o valor da variável TEMP no sistema operacional. Siga as etapas abaixo:

- Acesse as Variáveis de Ambiente clicando com o botão direito em "Este Computador" e selecione "Propriedades".

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056379894)

  

- Clique em "Configurações avançadas do sistema".

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056379994)

  

- Em seguida, clique em "Variáveis de Ambiente".

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056380494)

  

- Edite as variáveis TEMP e TMP para alocar o backup em outro disco, a fim de atualizar o TAF e o TSS.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056380954)

- Reinicie o servidor para que as modificações entrem em vigor.

- Após a atualização do TAF, se necessário, reverta as configurações da pasta temporária para o disco local C:.
