---
content_hash: 25151d9e6def9944782058d0d1a7b46c06c100e119397ad31505b1500fab0ead
fetched_at: '2026-06-28T21:35:23.482777+00:00'
page_id: '257622723'
product: fluig
source: tdn-fluig
title: Consumo de Banda
type: documentation
url: https://tdn.totvs.com/display/fluig/Consumo+de+Banda
version: 16
---

Atenção

Esta página foi revisada para considerar as novas configurações de server do Fluig para a atualização 1.6.

Caso possua uma atualização anterior do Fluig acesse: .

# Objetivo

---

O objetivo desta documentação é apresentar o consumo de banda das tarefas do fluig.

# Consumo de Banda

---

Para um usuário, o consumo de banda em tarefas comuns do Fluig são:

| Recurso | Trafegado |
| --- | --- |
| Login | 390 KB |
| Home WCM | 578 KB |
| Empresas | 703 KB |
| Home inicial vazia | 1,2 MB |
| Navegação de documentos | 1.1 MB |
| Edição atributos de documento | 1.1 MB |
| Visualização de documento | 1.3 MB |
| Central de Tarefas | 1.2 MB |
| Página de Processos | 975 KB |
| Visualização / Edição do processo | 1.1 MB |
| Aprendizado / Início | 1,9 MB |
| Execução de avaliação | 1,3 MB |
| Turma em andamento | 1,1 MB |
| Trilha em andamento (5 itens de trilha) | 1,9 MB |
| Treinamento em andamento | 1,1 MB |
| Catálogo de Disciplinas e Turmas | 8,8 KB |
| Catálogo de Trilhas e Treinamentos | 309 KB |

Importante

Em casos de integração do Fluig com o ERP e/ou softwares de terceiros onde as instalações tenham comunicação remota é necessário um *link* com no mínimo 1 Mbps entre as aplicações.

Para análise de *links* de internet, deve-se acionar otime de**Infra Services TOTVS**. Esta equipe oferece todo o apoio necessário através de reuniões de entendimento, visitas técnicas (quando necessário), dentre outros serviços. Entre em contato com o seu ESN para buscar orientações sobre como proceder e solicitar uma proposta.

# Documentos

---

Para documentos com tamanho médio de 500 KB, o uso de banda por usuário é de aproximadamente 20 KB/s.

# LMS

---

Referente à execução de conteúdos (vídeo, áudio, PDF, SCORM, etc.) no LMS do TOTVS Fluig Plataforma, deve ser considerado 1,1 MB para inicializar o *player* de conteúdo + tamanho do arquivo do conteúdo.

O tamanho dos conteúdos (imagens, vídeos, etc.), que é de responsabilidade do cliente, pode afetar o desempenho de execução desse conteúdo, dependendo da velocidade da conexão à *internet* do usuário.

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.

(function(f, b, g) {
var pageUrl = window.location.href;
var a = {
key: "1ed6b746ae3892da",
campaign: "8d9daeb2",
tags: {
"page": pageUrl
}
};
var e;
var c = f.getElementsByTagName(b)[0];
if (f.getElementById(g)) {
return
}
e = f.createElement(b);
e.id = g;
e.src = "https://cdn.tracksale.co/tracksale-js/tracksale.js";
e.type = "text/javascript";
e.async = true;
e.onload = e.onreadystatechange = function() {
var h = this.readyState;
try {
var d = new Tracksale();
d.init(a)
} catch (i) {}
};
c.parentNode.insertBefore(e, c)
}(document, "script", "tracksale-js"));
]]>
