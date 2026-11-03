---
article_id: 360026703731
category: Configurador
content_hash: adfd01eb6814d6ce48123c6ecc4a059bacae90a4fa0ab9be7f16228b001a3b51
fetched_at: '2026-06-28T22:42:18.914789+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Acerto de Numeração Automática
type: support-article
updated_at: '2024-05-08T11:34:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026703731-Framework-Linha-Protheus-Acerto-de-Numera%C3%A7%C3%A3o-Autom%C3%A1tica
---

**Dúvida**  
Como posso acertar a numeração automática quando ela sai de ordem por algum motivo?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 11  
  
**Solução**  
Caso exista uma inconsistência na ordem da numeração automática de alguma tabela, o primeiro passo é executar a rotina **APCFG110** pelo Configurador para acertar a ordem. Caso ainda não tenha essa rotina em seu menu, seguem abaixo os passos para criá-la:  
  
1. Acesse o Configurador > Ambiente > Cadastros > **Menu**2. Selecione somente o menu do **Configurador**, e clique em **OK**3. Adicione o menu para a coluna **Novo Menu**4. Selecione a **pasta** onde deverá ser criada a nova rotina  
  
5. Clique em **Novo Item**6. Preencha o **nome** que deseja para a rotina no menu  
  
7. Em **Programa** digite **APCFG110**8. Em **Módulo** selecione **Configurador**, e clique em **OK**9. Clique em **Gerar**, e selecione o nome para o menu (para manter o padrão, digite SIGACFG)  
  
10. Clique em **Gerar**11. Após criado o item de menu, saia do Configurador e entre novamente para visualizar a **nova rotina**Após ter criado a rotina no menu, acesse-a e siga os passos abaixo para acertar a numeração:

1. Acesse a rotina **APCFG110** no Configurador

2. Vamos tomar como exemplo uma numeração automática no campo A1\_COD da tabela de Clientes (**SA1**). Na imagem abaixo, note que existem 4 clientes cadastrados, portanto a última numeração é 000004:  
![2019-04-10_1001.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360025986251)

3. Na rotina **APCFG110**, a numeração deverá estar conforme a imagem abaixo:  
![2019-04-10_1002.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360025986271)

Na área **Números em uso / Números liberados**, irá aparecer o que deverá ser o próximo número quando alguém incluir um novo Cliente, neste caso, **000005**.

Na área **Próximos números** será exibido o número subsequente na ordem, neste caso, **000006**.

Se por algum motivo, ao incluir um Novo Cliente na rotina de Clientes, a próxima numeração não estiver sendo 000005, então você deve clicar 2 vezes no número que está em **Números em uso**, alterar para o que seria o próximo, e na área **Próximos números** inserir o subsequente correto. Com isso você redefine a ordem que o sistema de numeração automática deve seguir.

**Informação**  
Se houver uma numeração discrepante na sequência da tabela, como por exemplo, alguma numeração iniciada com uma letra, em meio a uma sequência de números (no banco de dados, as letras vem depois dos números, então o código iniciado com letra vai ser considerado o último número da sequência, depois de qualquer número), toda vez que o servidor for reiniciado, esse código virá incorreto. Desta forma, recomendamos abrir a tabela manualmente e efetuar a correção, caso seja possível. Caso tenha dúvidas nesse processo, favor entrar em contato com a equipe responsável pelo respectivo módulo responsável por esta tabela.

Maiores informações sobre numeração automática no link abaixo:  
<http://tdn.totvs.com/pages/viewpage.action?pageId=309411140>
