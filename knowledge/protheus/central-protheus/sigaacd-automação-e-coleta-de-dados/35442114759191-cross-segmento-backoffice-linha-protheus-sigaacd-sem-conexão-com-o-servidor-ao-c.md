---
article_id: 35442114759191
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1cf658a3255d5f958ed5fe6afd647ac71f34ca559771595df71f8c88ee3eabc6
fetched_at: '2026-06-28T22:39:13.812335+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Sem Conexão com o
  Servidor ao conectar com a conexão HTTPS
type: support-article
updated_at: '2025-10-06T17:28:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35442114759191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Sem-Conex%C3%A3o-com-o-Servidor-ao-conectar-com-a-conex%C3%A3o-HTTPS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35442114740631) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao acessar o aplicativo Meu Coletor de Dados na conexão HTTPS, apresenta a mensagem

"Sem Conexão com o Servidor" como solucionar?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Quando a conexão REST está configurada com certificado SSL para conexão HTTPS, a mesma depende do certificado estar instalado nos dispositivos que vão fazer o acesso, no caso do meu coletor isso também é verdadeiro.

[Porta Multiprotocolo - Geração de Certificado](https://tdn.totvs.com/x/Ro_vI)

A utilização do certificado gerado localmente não é indicada para outras finalidades que não seja o application server, se houver erros no momento de subir o serviço do REST, será necessário validar junto à certificadora da Empresa, os certificados apontados, onde para a aplicação do Appserver é importante que o certificado, e a chave privada estejam codificados no formato Apache (Base 64) com extensão (\*.PEM) ou (\*.CRT).

Entre em contato com sua certificadora para que seja fornecido o certificado neste formato.

Mais informações nos links abaixo:

[KeyServer](https://tdn.totvs.com/x/6Ypc)

[CertificateServer](https://tdn.totvs.com/x/5Ypc)

**ATENÇÃO :**   
O certificado padrão da TOTVS foi criado para comunicação Segura da Porta Multiprotocolo da conexão SmartClient Desktop com Appserver (Aplicação Protheus). Recomendamos que seja feito a compra com uma certificadora de sua preferência.

É possível sim, utilizar o certificado nos aplicativos fazendo a instalação do certificado no aparelho que vai ser utilizado para o coletor, no entanto é necessário realizar um ajuste adicional no certificado (CA=true) para atender regras do próprio Android.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
