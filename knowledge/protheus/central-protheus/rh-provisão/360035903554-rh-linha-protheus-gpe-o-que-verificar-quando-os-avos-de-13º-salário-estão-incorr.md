---
article_id: 360035903554
category: RH - Provisão
content_hash: deb39b9e174ca0036768b1586c9585f98a5c8161f93a37b671950405719a4f73
fetched_at: '2026-06-28T22:43:55.965112+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando os avos de 13º Salário estão
  Incorretos na provisão
type: support-article
updated_at: '2025-10-24T13:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035903554-RH-Linha-Protheus-GPE-O-que-verificar-quando-os-avos-de-13%C2%BA-Sal%C3%A1rio-est%C3%A3o-Incorretos-na-provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903790844311)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**O que verificar quando ao Calcular as Provisões os avos do 13º Salário estão incorretos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Ao calcular as **Provisões**, os avos de 13º Salário estão maiores do que o funcionário tem direito.  
Este incidente pode ocorrer quando o funcionário gozou Férias durante o ano.  
Para solucionar este incidente, é necessário confirmar se no cadastro da Ausência os campos referentes à Provisão de 13º Salário estão configurados de forma correta.   
  
Para correção realize os seguintes passos:

1. Acesse: Atualizações / Definição de Cálculo / **Tipos de Ausências** (**GPEA430**) / Localize o Tipo de Ausência **001 - Férias**  clique em Visualizar. Verifique se o campo "**Abat.Avos 13"** (RCM\_DECIMO) e "**Prov. 13º."** (RCM\_PROV13) estão configurados conforme o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046901454)

Caso esteja diferente, será necessário Recriar a tabela RCM - Tipos de Ausência.

2. Acesse o **Configurador** / Base de Dados / Dicionários / Bases de Dados / Localize a tabela RCM e clique na opção Alterar;  
  
3. Renomeie o nome da Tabela. No exemplo abaixo, a tabela RCM possui o nome RCMT10, altere para um nome que não exista em seu ambiente, RCMT10\_1 por exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046901994)

- Após a alteração, o campo Nome será alterado como RCMT10\_1. Clique em Confirmar.  
- Será apresentado o *browse*novamente. Clique no ícone com desenho Disquete. Será aberta uma nova janela, clique em Avançar em todas as janelas que forem mostradas.  
- Será apresentada a janela abaixo ao fim do processamento. Verifique se será apresentada a mensagem: **Atualização finalizada com sucesso** e clique em **Finalizar**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046902474)

4. Após a execução do processo acima acesse o módulo Gestão de Pessoal /Atualizações / Definição de Cálculo / Tipos de Ausência para que a tabela seja recriada. Vale lembrar que caso tenha algum campo customizado ou adequado para a sua base nos tipos de ausência, será necessário ajustá-los manualmente.  
  
5. Acesse o Cadastro do tipo de Ausência Férias, e confirme que os campos estão configurados corretamente, conforme o Passo 1.

6. Acesse Miscelânea / Provisões / **Provisões de Férias e 13º Salário**(**GPEA070**) / Selecione o Funcionário com cálculo de Provisões incorreto e Exclua o último cálculo das Provisões.  
Para mais informações sobre como Excluir os cálculos de Provisão [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-MP-GPE-Como-Excluir-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio).  

7. Calcule novamente as Provisões e confirme se os avos de 13º Salário estão corretos.

**Observação:** A mesma validação deve ser realizada para os demais Cadastros de Tipo de Ausência, quando houver mais afastamentos no ano corrente.

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
