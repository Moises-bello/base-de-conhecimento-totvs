---
article_id: 360051030814
category: RH - Funcionários
content_hash: 669789cfd1cf70bf627842499e773659d746cae22c72cbd0ddae6c09aa96891d
fetched_at: '2026-06-28T22:43:28.731599+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema valida no cadastro de funcionários
  campo RA_NOME quando ultrapassa 30 carácter
type: support-article
updated_at: '2021-07-16T21:29:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051030814-RH-Linha-Protheus-GPE-Como-o-sistema-valida-no-cadastro-de-funcion%C3%A1rios-campo-RA-NOME-quando-ultrapassa-30-car%C3%A1cter
---

**Dúvida**Como o sistema valida no cadastro de funcionários campo RA\_NOME quando ultrapassa 30 carácter?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Foi desenvolvido tratamento para este novo campo que irá conter o nome completo do funcionário sem nenhuma abreviação.

Quando o campo **RA\_NOMECMP** existir e estiver preenchido, será usado o seu conteúdo nos campos referentes ao **Nome**.

Esta implementação foi feita para quando houver necessidade de utilizar o campo **Nome** com mais de 30 caracteres.

Será utilizado somente na SEFIP e em mais nenhum outro ponto do Sistema.

Se o campo RA\_NOMECMP ultrapassar o tamanho de 40 caracteres, altere o tamanho do campo R9\_DESC para o tamanho do campo RA\_NOMECMP.

Na validação do campo RA\_NOMECMP deve ser colocada a função FHIST() para que o histórico de alteração deste campo seja gravado no SR9.

**Procedimentos:**

- Crie o campo RA\_NOMECMP com 70 caracteres;

- Coloque na validação do sistema a função FHIST();

- Aumente o tamanho do campo R9\_DESC para 70 caracteres;

- Preencha no Cadastro de Funcionários o campo RA\_NOMECMP e coloque no campo RA\_ALTNOME = **Sim**;

Processe a SEFIP e verifique se o conteúdo do campo RA\_NOMECMP foi levado para o arquivo texto.
