---
content_hash: 41391740aabf4e8c9ffa625cf80b997bce3165a9d9846ac3a77b9c47e5d581f6
fetched_at: '2026-06-29T00:12:02.274442+00:00'
page_id: '900450989'
product: rm
source: tdn-rm
title: Configurar tempo de timeout do portal
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurar+tempo+de+timeout+do+portal
version: 3
---

O objetivo desta documentação é auxiliar as instituições na configuração para **aumentar o tamanho time out** da ferramenta **IIS(Internet Information Services)**do portal **portal educacional**.

Conforme citado, a configuração de**tamanho time out** de uma requisição é uma medida de segurança para o servidor Web.

Sendo assim, **não é recomendado que se permita** requisições com tamanho muito grande. Em casos de ataques, como por exemplo uma negação de serviço, o envio de requisições de grande volume pode facilitar a ação de pessoas mal-intencionadas, tornando o servidor mais vulnerável.

Todas as informações apresentadas foram verificadas e testadas em um ambiente controlado. Contudo, devido à diversidade e complexidade das configurações, bem como às particularidades dos servidores de cada cliente, recomenda-se que as alterações sejam inicialmente realizadas em um ambiente de homologação.

**Os tamanhos máximos de upload** exibidos nas imagens abaixo são **meramente ilustrativos**.

## **CONFIGURAÇÕES**

**1)** Acesse o **IIS(Internet Information Services).**

Configuração padrão para todo os portais do FrameHTML

A configuração do **tamanho time out** para todos os sites que estão dentro do diretório do **FrameHTML**. Lembrando que esta opção inclui outros produtos da TOTVS, além do Educacional, caso o cliente possua.

* **Todos os portais, selecione a pasta: "**Sites\Default Web Site****"****

**As imagens abaixo são apenas um exemplo** utilizando a pasta padrão FrameHTML, **mas deverá selecionar a pasta conforme definido acima pela instituição**.

**3.** Selecione a opção **"Configurações Avançadas"**

**4.** Preencha com tempo desejado em "**Tempo Limite de Conexão (segundos)**"

**5)** Ao final do processo reinicia o IIS para efetivar todas as alterações
