---
article_id: 4477439959063
category: TAF - eSocial - Configuração
content_hash: 8924361cc7ccfa664ab0fd95a1646623e12ff2c50538caaff0471b6c4c455bae
fetched_at: '2026-06-28T22:45:14.300785+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como ativar a porta multi
  protocolo no TAF - MPP
type: support-article
updated_at: '2026-06-23T20:39:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4477439959063-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-ativar-a-porta-multi-protocolo-no-TAF-MPP
---

**Dúvida**Como ativar a porta multi protocolo no TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Porta Multi Protocolo - Todas as versões  
  
**Solução**

1 - Para ativar a porta multi protocolo no TAF, precisa estar com o TAF atualizado, de acordo com a documentação abaixo:  
[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-Expedi%C3%A7%C3%A3o-Cont%C3%ADnua)

***ATENÇÃO:** CLIENTES QUE POSSUÍREM **SLAVES,** AS PARAMETRIZAÇÕES CONFORME ORIENTAÇÃO ABAIXO **DEVERÁ SER APLICADA** NOS ARQUIVOS DE CONFIGURAÇÃO **PARA CADA SLAVE**.*

2 - Acesse a pasta de instalação do TAF e localize a pasta BIN/APPSERVER e abra o arquivo APPSERVER.INI;

3 - Na seção [DRIVERS] adicione os parâmetros:

MULTIPROTOCOLPORT=1  
MULTIPROTOCOLPORTSECURE=0

**Exemplo:**

```
[DRIVERS]  
ACTIVE=TCP  
MULTIPROTOCOLPORT=1  
MULTIPROTOCOLPORTSECURE=0
```

4 - Na seção [GENERAL] adicionar o parâmetro:  
APP\_ENVIRONMENT=nome\_do\_ambiente

**\*\* Não é possível utilizar mais de um ambiente na porta multi protocolo, no mesmo appserver.ini**

\*\* Inserir parâmetro para apenas um ambiente.

**Correto:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24308806618903)

**Errado:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24308830710807)

**Dica:** Para localizar o nome do ambiente basta localizar os parâmetros que indicam o caminho do SOURCEPATH do TAF. Geralmente por padrão o nome do ambiente é TAF conforme exemplo abaixo:

![blobid3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4477370075031)

Após localização do nome do ambiente adicione no parâmetro:  
APP\_ENVIRONMENT=TAF

5 - Acesse o Configurador do TAF e localize os parâmetros MV\_BACKEND e MV\_GCTPURL e limpe as URL's configuradas deixando em 'branco' os parâmetros para que o MPP entre em ação:  
 [TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)

6 - Reinicie os serviços do TAF (DBACCESS, APPSERVER e TAF-WS) e acesse o ambiente.

7 - O visual da tela de LOGIN muda o layout do acesso ao TAF:

![blobid4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4477343177751)

8 - O usuário ADMIN que não houver senha basta apertar a barra de espaço no teclado para habilitar o botão de acesso ao TAF:

![blobid5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4477362229143)
