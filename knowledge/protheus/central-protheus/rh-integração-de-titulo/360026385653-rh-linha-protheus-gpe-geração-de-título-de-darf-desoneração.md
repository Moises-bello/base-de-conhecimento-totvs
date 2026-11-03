---
article_id: 360026385653
category: RH - Integração de Titulo
content_hash: 7e2a3f0aa1674f1dd451dd2619b0fa73dd9aad90a56283a6dc4b1c9926bd11ea
fetched_at: '2026-06-28T22:43:37.212869+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Geração de título de DARF Desoneração
type: support-article
updated_at: '2025-08-13T17:55:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026385653-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-de-t%C3%ADtulo-de-DARF-Desonera%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34149143241495) Tempo aproximado para leitura: **00:03:00 min**  
  
Dúvida**Como efetuar a geração de título de Darf - Desoneração?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Versão 12.  
  
**Solução**Como gerar título de DARF Desoneração:  
  
**ATENÇÃO:** as configurações mostradas nos prints abaixo servem apenas para ilustrar o processo. Realize a configuração de acordo com as informações cadastradas de sua empresa.   
  
  
1) Acessar Miscelânea -> Títulos -> Definição e configurar um título, definindo a seleção padrão disponível : DARF - DESONERAÇÃO.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040867214)  
  
  
2) A tabela S037 deve estar cadastrada com as informações de recolhimento da empresa. O exemplo abaixo apresentaremos uma empresa com Desoneração Mista.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041699473)

3) Verifique se as informações da desoneração estão informadas na tabela S033 de acordo com a  competência:   
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041699693)

**Obs:** Todos os campos deverão ser preenchidos corretamente. Caso o valor para base de cálculo não esteja preenchido, a geração do título não será realizada.

Dúvidas de como cálculo a desoneração, acesse:  
[MP - GPE852 - GPEM013 - Como configurar o ambiente e conferir o cálculo da desoneração mista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011961451-MP-GPE852-GPEM013-Como-configurar-o-ambiente-e-conferir-o-c%C3%A1lculo-da-desonera%C3%A7%C3%A3o-mista?source=search)  
4) Após o cálculo da desoneração, caso o parâmetro MV\_RAT0973 esteja configurado como .T., será efetuada a gravação da verba de ID 0973 na tabela SRC (folha aberta/SRD folha fechada).  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041701673)  
  
  
5) Acesse Relatórios> Periódicos> Darf/PIS e efetue a geração da darf contribuição previdenciária para conferência dos valores:   
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041702033)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041702153)

6) Após realização do passo a passo descrito, faremos a geração do título de DARF Desoneração através da rotina GPEM650, configurando os campos do grupo de perguntas de acordo com a competência do mês:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041741173)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041741213)  
  
7) Acesse Miscelânea -> Títulos -> Manutenção e verifique o valor do título gerado de acordo com desoneração calculada:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041741293)  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
