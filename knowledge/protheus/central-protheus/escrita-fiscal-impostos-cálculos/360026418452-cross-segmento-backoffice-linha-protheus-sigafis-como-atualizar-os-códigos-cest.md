---
article_id: 360026418452
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 48699313b47fcaa2c8a996c39cc95acc7d1d490948f735ab5bc1a15c5eb2e7a0
fetched_at: '2026-06-28T22:39:30.478701+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAFIS- Como atualizar os códigos
  CEST?
type: support-article
updated_at: '2023-12-13T20:57:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026418452-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIS-Como-atualizar-os-c%C3%B3digos-CEST
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19814332500503) Tempo aproximado para leitura: 00:02:10 min**

**Dúvida**

Como atualizar os códigos CEST? campo para preenchimento do produto B1\_CEST

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para alterar ou incluir algum cadastro relacionados ao códigos CEST utilize a rotina Código Cest (FISA131)

Documentação.

<http://tdn.totvs.com/pages/releaseview.action?pageId=260014602>

Se não possuir a rotina no menu, basta incluir pelo configurador.

**Não é possível inserir o valor NULL na coluna 'B1\_CEST', tabela 'SB1010'; a coluna não permite nulos. Falha em INSERT.**

Foram ajustados os campos B1\_CEST (Ajuste do tamanho para 7 caracteres, inclusão de validação, consulta padrão F0G e amarração na tabela SX9) e CIU\_CEST (Inclusão de validação).

Esta correção será disponibilizada na Expedição contínua de Outubro/2023 e o pacote poderá ser acessado através dos links disponibilizados na documentação [Pacotes de Atualização - Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=525823851).  
  
Informações sobre a Expedição contínua acessar: [http://tdn.totvs.com/x/H4uCEw](https://tdn.totvs.com/x/H4uCEw).  
  
Informações sobre o compatibilizador UPDDISTR acessar: [Atualizador de dicionário e base de dados - UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=181965468).

Relacionado: [CFGTRIB - Configurador de Tributos - 12.1.22.10](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

**Saiba mais**:

[Protheus fiscal temas e parametros](https://tdn.totvs.com/display/public/PROT/Fiscal+-+Protheus+12)
