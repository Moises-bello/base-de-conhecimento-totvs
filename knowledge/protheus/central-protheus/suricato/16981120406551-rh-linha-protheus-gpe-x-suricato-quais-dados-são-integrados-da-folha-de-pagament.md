---
article_id: 16981120406551
category: Suricato
content_hash: 95449075343d00db0232df3b9dc16f88c5ce883b616c6c836260cac318f423f1
fetched_at: '2026-06-28T22:44:57.379765+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - GPE x Suricato - Quais dados são integrados da Folha
  de Pagamento para o Suricato
type: support-article
updated_at: '2023-12-20T13:10:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16981120406551-RH-Linha-Protheus-GPE-x-Suricato-Quais-dados-s%C3%A3o-integrados-da-Folha-de-Pagamento-para-o-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981129217559) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Quais dados são integrados da Folha de Pagamento para o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir da versão 12.1.23  
  
**Solução**Os dados integrados da **Folha de Pagamento** para o **Suricato**, são os listados abaixo:**Empresas/Filiais**Ao incluir ou alterar uma empresa/filial no Cadastro de Empresa, deve-se executar novamente o processo de Carga Inicial de Empresa, Unidade e Lotação para atualização da informação da empresa/filial no Suricato.  
  
**Cadastro de Funcionário**Ao realizar a admissão de um funcionário ou alteração de seus dados no Cadastro do Funcionário, o mesmo será integrado com o Suricato. Para confirmar se a integração foi realizada, verifique se o Cadastro de Funcionário no Suricato foi atualizado.  
Observação: Por meio do parâmetro MV\_TSAIURB, é possível definir se será enviado o crachá do funcionário do Protheus para o Cadastro de funcionário do Suricato.  
  
**Cadastro de Cargo/Função**Ao realizar a inclusão, alteração ou exclusão de uma função no Cadastro de Funções, a função será integrada com o Suricato. Também será integrada a troca de função de um funcionário. Se for realizada a troca de função, essa informação será integrada com o Suricato e ele irá manter histórico da função anterior e da atual. Para confirmar se a integração foi realizada, verifique no Suricato se o Cadastro de Cargo ou o Cadastro do Funcionário foram atualizados.  
  
**Cadastro de Turno de Trabalho**Ao incluir um turno de trabalho no Cadastro de Turnos de Trabalho, não haverá integração do turno com o Suricato, pois é necessário o preenchimento da tabela de horário padrão. Caso seja realizada a troca de turno do Funcionário, a mesma será integrada e o Suricato irá manter histórico do turno anterior e do atual. Para confirmar se a integração foi realizada, verifique no Suricato se a Escala, Horário da Escala ou o Cadastro do funcionário foram atualizados.  
  
**Cadastro de Sindicato**Ao realizar a inclusão, alteração ou exclusão de um sindicato no Cadastro de Sindicatos, ele será integrado com o Suricato. Para confirmar se a integração foi realizada, verifique se o cadastro de Pessoa Jurídica no Suricato foi atualizado.  
  
**Cadastro de Afastamentos**Ao realizar a inclusão, alteração ou exclusão de um afastamento para o Funcionário, ele será integrado com o Suricato. Para confirmar se a integração foi realizada, verificar se o cadastro de Afastamentos no Suricato foi atualizado.  
  
**Cadastro de Centros de Custo**Ao realizar a inclusão, alteração ou exclusão de um Centro de Custo no Cadastro de Centros de Custos, ele será integrado com o Suricato. Para confirmar se a integração foi realizada, verifique se o cadastro de Centro de Custos no Suricato foi atualizado.  
  
**Cadastro de Transferências**Ao realizar a transferência de um Centro de Custo de um funcionário, essa informação será integrada, alterando o cadastro do funcionário no Suricato. O Suricato irá manter histórico do centro de custo anterior e do atual.  
Quando a transferência de um funcionário for entre Empresas/Filiais o cadastro do funcionário no Suricato será atualizado.  
Observação: O Suricato manterá os dois registros do funcionário (devido mudança na chave externa), onde o registro anterior terá data de demissão com um dia anterior ao da transferência e o crachá ficará em branco, e o registro atual manterá o crachá do usuário.  
Para confirmar se a integração foi realizada, verifique se o cadastro de Funcionário no Suricato foi atualizado.  
  
**Cálculo de Férias**Ao realizar o cálculo de férias para um funcionário, o cadastro do funcionário no Suricato será atualizado com a informação do afastamento. Para confirmar se a integração foi realizada, verifique se o cadastro de Funcionário no Suricato foi atualizado.  
  
**Cálculo de Rescisão**Ao realizar o cálculo de rescisão para um funcionário, essa informação será integrada atualizando a informação sobre o desligamento do funcionário no Suricato.  
Ao excluir o cálculo de rescisão, a mesma será integrada, atualizando o funcionário no Suricato.  
Para confirmar se a integração foi realizada, verifique se o cadastro do funcionário foi atualizado.  
  
**Cadastro de Regra de Apontamento**Ao alterar o intervalo móvel de uma regra na rotina de Cadastro de Regras de Apontamento, o campo Tipo de Escala no Cadastro de Escala no Suricato será atualizado.  
  
**Saiba Mais:**  
[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779731236119)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
