---
article_id: 7569207525143
category: MDT - eSocial
content_hash: add405ffad2af9284501c8ed23f9b53453a451d8e086ff0b7fb4c44bd3f15a71
fetched_at: '2026-06-28T22:44:29.361200+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Em que cenários os eventos de SST não
  serão comunicados ao Governo
type: support-article
updated_at: '2025-08-05T17:31:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7569207525143-RH-Linha-Protheus-MDT-eSocial-Em-que-cen%C3%A1rios-os-eventos-de-SST-n%C3%A3o-ser%C3%A3o-comunicados-ao-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25674248589719) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Em que cenários os eventos de SST não serão comunicados ao Governo?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**

Para a geração dos eventos de SST no eSocial (S-2210, S-2220, S-2221 e S-2240), algumas condições precisam ser atendidas. Caso alguma dessas condições não seja satisfeita, os eventos de SST não serão enviados. São elas:

* Funcionários com categoria (RA\_CATEFD) incluída no parâmetro MV\_NG2NENV;
* Funcionários com categoria (RA\_CATEFD) incluída no parâmetro MV\_NTSV;
* Funcionários em admissão preliminar (S-2190) cujo leiaute seja anterior à versão S-1.0 simplificada;
* Funcionários sem exposição a agentes nocivos, quando a data de envio dos eventos S-2220 e S-2240 for anterior à data definida no parâmetro MV\_NG2DENO.

* **Funcionários com categoria contida no parâmetro MV\_NG2NENV:**

Os funcionários que possuem sua categoria (RA\_CATEFD) contida no parâmetro MV\_NG2NENV não tem os eventos de SST enviados ao SIGATAF/Middleware. O parâmetro foi criado para permitir um maior controle sobre quais funcionários efetivamente serão comunicados e possibilitar que para algumas categorias de funcionários, os eventos não sejam integrados.

Para saber mais sobre o parâmetro MV\_NG2NENV acesse: [Novo Controle de Envio dos Eventos de SST - Parâmetro MV\_NG2NENV](https://tdn.totvs.com/x/YwZ0JQ).

* **Funcionários com categoria contida no parâmetro MV\_NTSV:**

Os funcionários que possuem sua categoria (RA\_CATEFD) contida no parâmetro MV\_NTSV não tem o evento S-2300 comunicado ao Governo, devido o envio desse evento ser opcional para algumas categorias de trabalhadores sem vínculo. Como os funcionários com a categoria contida no parâmetro não tem o evento S-2300 enviado, não é possível realizar o envio dos eventos de SST, uma vez que é necessário o envio preliminar do evento S-2190, S-2200 ou S-2300 obrigatoriamente.

Para saber mais sobre o parâmetro MV\_NTSV acesse: [Controle de autônomos - Parâmetro MV\_NTSV](https://tdn.totvs.com/x/xwVYGw).

* **Funcionários em admissão preliminar e leiaute na versão anterior a S-1.0 simplificada:**

Os funcionários que estão em admissão preliminar (S-2190) no leiaute anterior ao S-1.0 simplificado, não tem algumas informações comunicadas ao Governo. Um exemplo é a tag <matricula> do evento S-2190 que não existe no leiaute 2.5, e como é uma tag necessária para a comunicação dos eventos de SST, não se torna possível realizar o envio. Caso o leiaute esteja definido na versão S-1.0 simplificada, o envio poderá ocorrer normalmente visto que a tag <matricula> existe para esse cenário.

* **Funcionários sem exposição a agentes nocivos com a data de envio dos eventos S-2220 e S-2240 menor que a data definida no parâmetro MV\_NG2DENO:**

Os funcionários que não estão expostos a agentes nocivos não tem a obrigação de envio dos eventos S-2220 e S-2240 antes da implantação efetiva do PPP eletrônico. Dessa forma foi criado o parâmetro MV\_NG2DENO para definir a partir de qual data os eventos S-2220 e S-2240 devem começar a ser comunicados ao SIGATAF/Middleware para os funcionários sem exposição a agentes nocivos.

Para saber mais sobre o parâmetro MV\_NG2DENO acesse: [Parâmetro MV\_NG2DENO para definir o início de envio dos eventos não obrigatórios para funcionário Sem Exposição](https://tdn.totvs.com/x/xwZEK).  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
