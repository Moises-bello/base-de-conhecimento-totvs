---
article_id: 360053286773
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 5a683282cf5be5b5c061a0228ea0bcefb363303b5e1b561651c2dbccb5877327
fetched_at: '2026-06-28T22:45:21.089253+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - TSS - Erro transmitir ao e-Social: WSCERR044/Não
  foi possível POST'
type: support-article
updated_at: '2024-09-24T14:11:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053286773-RH-Linha-Protheus-TAF-eSocial-TSS-Erro-transmitir-ao-e-Social-WSCERR044-N%C3%A3o-foi-poss%C3%ADvel-POST
---

**Dúvida**

Ao transmitir os eventos para o e-Social ou quando se faz necessário atualizar o Certificado Digital, ocorre o erro conforme abaixo:

*WSCERR044 / Não foi possível POST: URL <https://webservices.envio.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc> ( -1 : UNKNOW ERROR (WIN) )*

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - TSS - Todas as versões

**Solução**

1 -  Verifique a URL do Servidor onde está instalado o TSS e vá na pasta de instalação do TSS e na pasta **bin/appserver**, abra o arquivo **appserver.ini;**

2 - Ao abrir o arquivo, confira a porta de conexão na seção [HTTP]:

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086531693)

3 - Abra o navegador(Browser) e insira sua URL com a porta configurada no arquivo appserver e verifique se a mesma está ativa.

**Exemplo:**

*<http://localhost:8080> ou <http://192.168.1.1:8080>*

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085334114)

4 - Se não aparecer a mensagem no navegador acima, verifique se na máquina possui algum bloqueio. Caso possuir Proxy, certifique-se de que está configurado conforme documentação:

<https://tdn.totvs.com/pages/releaseview.action?pageId=321290594>

5 - Acesse o Configurador do TAF:

[TAF - CONFIGURADOR - Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413)

6 - No configurador, nas opções: Ambiente -> Email/Proxy, verifique se os campos referente ao Proxy estão em branco, se caso não possuírem proxy:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086531833)

**Obs.:** Se caso não houver configuração do proxy e tiver algum parâmetro preenchido, pode remover as informações!

7 - No Configurador ainda, em: Ambiente -> Cadastros -> Parâmetros:

[TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)

8 - Altere o parâmetro MV\_TAFSURL e insira a URL de configuração do TSS como no exemplo da imagem abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086531893)

9 - Saia do Configurador e acesse o SIGATAF, realize novamente a configuração do Certificado Digital:

[RH - Linha Protheus - TAF - eSocial - Configuração - TSS - Certificado Digital A1 - Como Efetuar Preparação do Certificado Digital e Configurá-lo no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034159554-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-TSS-Certificado-Digital-A1-Como-Efetuar-Prepara%C3%A7%C3%A3o-do-Certificado-Digital-e-Configur%C3%A1-lo-no-TAF)
