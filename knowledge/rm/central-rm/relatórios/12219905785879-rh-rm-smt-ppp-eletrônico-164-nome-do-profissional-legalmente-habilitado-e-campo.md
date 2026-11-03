---
article_id: 12219905785879
category: Relatórios
content_hash: d5e3b01182790fa0e865015d725ed0d1b3f3cb3e6e4edcdf9d6b962f7a68cd22
fetched_at: '2026-06-28T22:47:43.389753+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: RH - RM - SMT - PPP Eletrônico  16.4 - Nome do Profissional Legalmente Habilitado
  e campo 18 - Representante Legal da Empresa
type: support-article
updated_at: '2025-12-01T18:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12219905785879-RH-RM-SMT-PPP-Eletr%C3%B4nico-16-4-Nome-do-Profissional-Legalmente-Habilitado-e-campo-18-Representante-Legal-da-Empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034548838551) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao gerar o relatório do PPP no site Meu INSS o campo 18 - Representante Legal da Empresa fica em branco. Como enviar os dados do Responsável Legal para o site do meu INSS?    
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - 12.1.34.221, 12.1.2205.161,  12.1.2209.106 e superiores.

**Solução**

A partir do 01/01/2023 o relatório PPP passou a ser emitido exclusivamente por meio eletrônico. Na prática, o evento S-2240 substitui o que corresponde ao histórico laboral do trabalhador, contendo informações como atividade exercida, agentes nocivos (exposição, intensidade e concentração) e outros dados. Assim o PPP eletronico se trata de um espelho de S-2240 e alguns dados no evento não é enviado conforme o layout do eSocial.  
  
**16.4 - Nome do Profissional Legalmente Habilitado**Conforme o layout do evento S-2240, no mesmo náo levado o nome do responsavel somente o Número de inscrição no órgão de classe. Assim ao gerar o relatório do site do Meu INSS o campo é emitido em branco.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12318743826583)****18 - Representante Legal da Empresa**  
No evento, não é solicitado os dados representante legal, assim esta informação não é enviada para a base do INSS. Assim ao gerar o relatório do site do Meu INSS o campo é emitido em branco.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12219550754327)

Caso tenha duvidas sobre o preenchimento do campo, orientamos que entre em contato com a central de atendimento do INSS através do numero 135. Ou entrar em contato com a central de atendimento do eSocial, no link abaixo contém as informações de como realizar o contato:

[Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432-RH-RM-FOP-eSocial-Contato-com-o-Governo-para-d%C3%BAvidas-sobre-os-eventos-do-eSocial)  
  
**Saiba Mais:**  
- [Como Emitir PPP Eletrônico - Perfil Profissiográfico Previdenciário](https://www.gov.br/pt-br/servicos/emitir-ppp-eletronico-perfil-profissiografico-previdenciario#quem-pode-utilizar-este-servico)  
[- PPP – Perfil Profissiográfico Previdenciário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719230)

[- Disponibilização do Perfil Profissiográfico Previdenciário (PPP) Eletrônico](https://www.gov.br/esocial/pt-br/noticias/disponibilizacao-do-perfil-profissiografico-previdenciario-ppp-eletronico)  
[- S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#evtExpRisco)
