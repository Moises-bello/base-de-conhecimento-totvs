---
article_id: 26159644908439
category: MDT - Atendimento Médico
content_hash: 201520de990bf8c352f5333fec50a6011e58b3249aabbea066516656c6355f06
fetched_at: '2026-06-28T22:44:20.411264+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Erro ao incluir Atestado ASO em ambiente INFORMIX
type: support-article
updated_at: '2025-08-14T19:26:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26159644908439-RH-Linha-Protheus-MDT-Erro-ao-incluir-Atestado-ASO-em-ambiente-INFORMIX
---

**![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26159683464727) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Ao incluir Atestado ASO em base INFORMIX, é apresentado error.log "erro no parâmetroFWFormModel: O código do formulário 'NT3MASTER' não foi encontrado on FWFORMMODEL:GETVALUE(FWFORMMODEL.PRX)".  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**  
Essa falha ocorre, se a consulta padrão do campo '**TM5\_FORNEC**' for customizada de forma incorreta pelo usuário.  
  
**Solução**No módulo SIGACFG (Configurador), deverá acessar o menu Base de Dados> Dicionário > Base de Dados e buscar pela tabela **TM5**, filtre o campo **TM5\_FORNEC**.  
  
Na aba Opções, valide se a **Consulta Padrão** esta apontando para a tabela **NGE- Fornecedor**.  
  
Caso o campo esteja apontando para *SIGAJURI* esta **incorreto** e deverá ajustar conforme imagem:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26159644890775)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
